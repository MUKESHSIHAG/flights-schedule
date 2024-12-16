# Flights by Country

This project fetches and displays the number of flights arriving at a given airport, grouped by country. It consists of a **backend** powered by FastAPI and a **frontend** using simple HTML and Bootstrap.

---

## Folder Structure

```
flights-by-country/
├── backend/                 # Backend API using FastAPI
│   ├── main.py              # FastAPI application file
│   ├── requirements.txt     # Python dependencies
├── frontend/                # Frontend for displaying data
│   ├── index.html           # Main frontend file
```

---

## Setup and Usage

### 1. Backend Setup

1. Navigate to the `backend/` folder:
   ```bash
   cd backend
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

6. The server will run at `http://127.0.0.1:8000` by default.

### 2. Frontend Setup

1. Navigate to the `frontend/` folder.
2. Open the `index.html` file in web browser.
3. Interact with the UI by entering a 3-character IATA airport code to view the results.

---

## Usage Flow
1. Start the backend server as described above.
2. Open the `index.html` file in your browser.
3. Enter a valid 3-character airport code (e.g., `LAX`, `SIN`).
4. View the table displaying the number of flights arriving from each country.

---

## Notes
- Ensure the backend server is running before testing the frontend functionality.
