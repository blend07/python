from fastapi import FastAPI
from models import Developer, Project

app = FastAPI()

@app.post("/developers/")
def create_developer(developer: Developer):
    return{"message": "Developer created succesfully", "developer": developer}

@app.post("/projects/")
def create_project(project: Project):
    return{"message": "Project created succesfully", "project": project}