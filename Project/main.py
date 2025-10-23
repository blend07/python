from fastapi import FastAPI
from models import Developer, Project

app = FastAPI()

@app.post("/developers/")
def create_developer(developer: Developer):
    return{"message": "Developer created succesfully", "developer": developer}

@app.post("/projects/")
def create_project(project: Project):
    return{"message": "Project created succesfully", "project": project}

@app.get("/projects/")
def get_project():
    sample_project = Project (
        title = "Sample Project",
        description = "This is a description",
        languages = ["Python", "Java"],
        lead_developer = Developer(name="John Doe", experience = 5)
    )
    return{}