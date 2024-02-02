from fastapi import FastAPI, Form, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import mysql.connector
from dotenv import load_dotenv
import os
import uvicorn

load_dotenv()  # Load environment variables

# Create the FastAPI instance
app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


def get_db_connection():
    return mysql.connector.connect(
        host="db", # because we are inside docker compose, we can use the service name as the host name
        user="root",
        password=os.getenv('MYSQL_ROOT_PASSWORD'),
        database=os.getenv('MYSQL_DATABASE')
    )


@app.get("/items", response_class=HTMLResponse)
async def get_items(request: Request):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM items")
    items = cursor.fetchall()
    cursor.close()
    conn.close()
    return templates.TemplateResponse("items.html", {"request": request, "items": items})


@app.post("/items", response_class=HTMLResponse)
async def add_item(request: Request, name: str = Form(...), description: str = Form(""), price: float = Form(...)):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO items (name, description, price) VALUES (%s, %s, %s)", (name, description, price))
        conn.commit()
        cursor.close()
        conn.close()
        return await get_items(request)
    except mysql.connector.Error as err:
        return templates.TemplateResponse("error.html", {"request": request, "message": str(err)})


@app.post("/items/update", response_class=HTMLResponse)
async def update_item(request: Request, id: int = Form(...), name: str = Form(None), description: str = Form(None),
                      price: float = Form(None)):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        update_data = []
        sql_update_query = "UPDATE items SET "
        if name:
            sql_update_query += "name = %s,"
            update_data.append(name)
        if description:
            sql_update_query += "description = %s,"
            update_data.append(description)
        if price is not None:
            sql_update_query += "price = %s,"
            update_data.append(price)

        # Remove trailing comma
        sql_update_query = sql_update_query.rstrip(',')
        sql_update_query += " WHERE id = %s"
        update_data.append(id)

        cursor.execute(sql_update_query, tuple(update_data))
        conn.commit()
        cursor.close()
        conn.close()

        if cursor.rowcount == 0:
            return templates.TemplateResponse("error.html", {"request": request, "message": "no item found with that id"})

        return await get_items(request)
    except mysql.connector.Error as err:
        return templates.TemplateResponse("error.html", {"request": request, "message": str(err)})


@app.get("/", response_class=HTMLResponse)
def get_root_html(request: Request) -> HTMLResponse:
    """
    Hmmm, what does this do? What is a template response? How can it help us?
    Renders the index.html template, with the request object passed in.
    :param request:
    :return:
    """
    return templates.TemplateResponse('index.html', {'request': request})


@app.get("/basics", response_class=HTMLResponse)
def get_basics_html(request: Request) -> HTMLResponse:
    return templates.TemplateResponse('basics.html', {'request': request})


@app.get("/css", response_class=HTMLResponse)
def get_css_html(request: Request) -> HTMLResponse:
    return templates.TemplateResponse('css.html', {'request': request})


@app.get("/fast_api", response_class=HTMLResponse)
def get_fast_api_html(request: Request) -> HTMLResponse:
    return templates.TemplateResponse('fast_api.html', {'request': request})


@app.get("/view_notes", response_class=HTMLResponse)
def get_view_notes_html(request: Request) -> HTMLResponse:
    return templates.TemplateResponse('notes.html', {'request': request})


@app.get("/web_development", response_class=HTMLResponse)
def get_web_development_html(request: Request) -> HTMLResponse:
    return templates.TemplateResponse('web_development.html', {'request': request})

@app.get("/web_serving", response_class=HTMLResponse)
def get_web_serving_html(request: Request) -> HTMLResponse:
    return templates.TemplateResponse('web_serving.html', {'request': request})





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
async def get_demo(request: Request) -> HTMLResponse:
    return templates.TemplateResponse('slowdemo.html', {'request': request})



@app.get("/slowroute")
async def slow_route():
    await asyncio.sleep(3)  # Artificial delay
    return {"message": "Delayed response received"}

@app.get("/timezones")
async def get_timezone():
    await asyncio.sleep(1);
    return {"timezone": ['CST', 'PST']}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
