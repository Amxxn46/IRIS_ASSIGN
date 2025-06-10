
# CapBudget FastAPI Application

This is a FastAPI app that reads data from an Excel sheet and provides APIs to list table names, get row details, and calculate row sums.

---

## How to Install and Run

1. **Download or unzip** the project folder.

2. **Open a terminal** or command prompt and go to the project folder.

3. (Optional) Create a virtual environment:
   - On macOS/Linux: run `python -m venv venv` and then `source venv/bin/activate`
   - On Windows: run `python -m venv venv` and then `venv\Scripts\activate`

4. **Install the required packages** by running:
   - `pip install -r requirements.txt`

5. **Make sure your Excel file** named `capbudg.xls` is placed inside the `Data` folder.

6. **Start the server** by running:
   - `uvicorn main:app --host 127.0.0.1 --port 9090 --reload`

7. **Open your browser** and go to:
   - `http://localhost:9090/docs` to use the API with Swagger UI.

---

## Available API Endpoints

- `/list_tables` – Shows all table names in the Excel sheet.
- `/get_table_details?table_name=...` – Lists the row names for a specific table.
- `/row_sum?table_name=...&row_name=...` – Calculates the sum of numbers in a given row.

---

## Testing

You can use Postman to test the APIs. A Postman collection file named `CapBudget.postman_collection.json` is included in the project.
