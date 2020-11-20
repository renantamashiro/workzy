import json
import os


jobs = os.getcwd() + "/.jobs.json"

def load() -> dict:
    with open(jobs, "r") as file:
        data = file.read()
    return json.loads(data)

def write(data: dict):
    with open(jobs, "w") as file:
        file.write(json.dumps(data, skipkeys=True, indent=2))

def create():
    with open(jobs, "w+") as  file:
        file.close()