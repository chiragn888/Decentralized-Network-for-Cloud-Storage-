from pathlib import Path

from fastapi import FastAPI

app = FastAPI()

@app.get("/license")
def get_license():
    license_path = Path(__file__).parent.parent / 'LICENSE'
    return license_path.read_text()

@app.get("/readme")
def get_readme():
    readme_path = Path(__file__).parent.parent / 'README.md'
    return readme_path.read_text()
