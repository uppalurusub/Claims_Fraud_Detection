from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "outputs"
print(DATA_DIR)
print(OUTPUT_DIR)

CLAIMS_FILE = DATA_DIR / "claims.csv"
