from pathlib import Path
import sqlite3

APP_DIR = Path.home() / ".expense_tracker"

APP_DIR.mkdir(parents=True, exist_ok=True)

DB_PATH = APP_DIR / "expenses.db"

conn = sqlite3.connect(DB_PATH)