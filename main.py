from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import JSONResponse
import pandas as pd
import xlrd
from typing import List, Dict
import os

app = FastAPI(title="Excel Table API", docs_url="/docs")

EXCEL_FILE_PATH = "./Data/capbudg.xls"

# Cache tables after first load
tables_cache: Dict[str, pd.DataFrame] = {}

def load_excel_sheets(file_path: str) -> Dict[str, pd.DataFrame]:
    try:
        return pd.read_excel(file_path, sheet_name=None)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading Excel: {e}")

@app.on_event("startup")
def startup_event():
    global tables_cache
    if os.path.exists(EXCEL_FILE_PATH):
        tables_cache = load_excel_sheets(EXCEL_FILE_PATH)
    else:
        raise FileNotFoundError(f"Excel file not found at {EXCEL_FILE_PATH}")

@app.get("/list_tables", tags=["Tables"])
def list_tables():
    return {"tables": list(tables_cache.keys())}

@app.get("/get_table_details", tags=["Tables"])
def get_table_details(table_name: str = Query(...)):
    if table_name not in tables_cache:
        raise HTTPException(status_code=404, detail="Table not found.")
    df = tables_cache[table_name]
    first_column = df.iloc[:, 0].dropna().tolist()
    return {"table_name": table_name, "row_names": first_column}

@app.get("/row_sum", tags=["Tables"])
def row_sum(table_name: str = Query(...), row_name: str = Query(...)):
    if table_name not in tables_cache:
        raise HTTPException(status_code=404, detail="Table not found.")
    df = tables_cache[table_name]

    row_data = df[df.iloc[:, 0] == row_name]
    if row_data.empty:
        raise HTTPException(status_code=404, detail="Row not found.")

    numeric_values = pd.to_numeric(row_data.iloc[0, 1:], errors='coerce')
    total = numeric_values.dropna().sum()

    return {
        "table_name": table_name,
        "row_name": row_name,
        "sum": float(total)
    }
