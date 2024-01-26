import multipart
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
import asyncio


# Create the FastAPI instance
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
def get_root_html() -> HTMLResponse:
    with open("templates/index.html") as html:
        return HTMLResponse(content=html.read())


@app.get("/basics", response_class=HTMLResponse)
def get_basics_html() -> HTMLResponse:
    with open("templates/basics.html") as html:
        return HTMLResponse(content=html.read())


# add the remaining endpoints here

@app.get("/notes")
async def read_notes():
    """
    Read the notes from the file and return them.
    :return:
    """
    try:
        with open("notes.txt", "r") as file:
            content = file.read()
    except FileNotFoundError:
        content = "No notes yet."
    return {"notes": content}


@app.post("/notes")
async def write_notes(note: str = Form(...)):
    """
    Write the notes to the file. post your messages to the notes endpoint.
    :param note:
    :return:
    """
    with open("notes.txt", "w") as file:
        file.write(note)
    return {"message": "Note saved successfully."}


# an example of a path parameter
@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/slowdemo")
async def get_demo():
    with open("templates/slowdemo.html") as html:
        return HTMLResponse(content=html.read())


@app.get("/slowroute")
async def slow_route():
    await asyncio.sleep(3)  # Artificial delay
    return {"message": "Delayed response received"}


def getStocks():

    html = """
    <html>
        <head>
            <title>Stocks</title> 
            </head>"""
    return {"stocks": ['AAPL', 'GOOG', 'TSLA']}
@app.get("/timezones")
async def get_timezone():
    await asyncio.sleep(1);
    return {"timezone": ['CST', 'PST']}

@app.get("/css")
async def get_css():
    with open("templates/css.html") as html:
        return HTMLResponse(content=html.read())

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
