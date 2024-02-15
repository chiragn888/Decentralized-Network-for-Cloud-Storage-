from pathlib import Path

from fastapi import FastAPI

app = FastAPI()

@app.get("/readme")
def read_readme():
    readme_path = Path('../README.md')
    return readme_path.read_text()

@app.get("/license")
def read_license():
    license_path = Path('../LICENSE')
    return license_path.read_text()
