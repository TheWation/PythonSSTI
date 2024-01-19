from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from jinja2 import Environment

app = FastAPI()

@app.get("/")
async def read_root(username=None):

    username = username or "Guest"
    Jinja2 = Environment()

    # Vulnerable Implementation
    output = Jinja2.from_string("Welcome " + username + "!").render()

    # Safe Implementation
    # output = Jinja2.from_string("Welcome {{ user_name }}!").render(user_name=username)

    return HTMLResponse(content=output)