from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import requests
from pydantic import BaseModel
from typing import Dict
import json
from collections import Counter
from fastapi.responses import JSONResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

API_KEY = "67601bb0cb1f933f72c63485"
BASE_URL = "https://api.flightapi.io/compschedule"
MODE="arrivals"
day=1

class AirportCodeQuery(BaseModel):
    airport_code: str

@app.get("/flights")
def get_flights(airport_code: str):
    url = f"{BASE_URL}/{API_KEY}?mode={MODE}&iata={airport_code}&day={day}"
    if len(airport_code)!=3:
        return {"success": False, "message": "Airport code should have length of 3"}
    try:
        print("fetching...")
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        city_counts = Counter()

        # Extract country names and the count
        for entry in data:
            arrivals = entry.get("airport", {}).get("pluginData", {}).get("schedule", {}).get("arrivals", {}).get("data", [])
            for arrival in arrivals:
                city = arrival.get("flight", {}).get("airport", {}).get("origin", {}).get("position", {}).get("country", {}).get("name")
                if city:
                    city_counts[city] += 1

        result = [
            {"Country": city, "# of Flights": count}
            for city, count in city_counts.most_common()
        ]

        return JSONResponse(content={"success": True, "data": result})

    except Exception as e:
        return {"success": False, "message": "There is some error"}
