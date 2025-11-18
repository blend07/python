from fastapi import FastAPI
from models import Developer, Project

app = FastAPI()

@app.post("/developers/")
def create_Developer(developer:Developer):
    return{"messagee":"Developer created succesfully", "developer" :developer}

@app.post("/projects/")
def create_project(project:Project):
    return{"message":"Project created succesfully", "project":project}


@app.get("/projects/")
def get_projects():
    sample_project = Project(
        title="Sample Project",
        description="This is a sample project",
        languages=["Python","FastAPI"],
        lead_developer=Developer(name="Alice",experience=5)
    )
    return {"projects":[sample_project]}

