import asyncio

from fastapi import FastAPI, Form, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import mysql.connector
from dotenv import load_dotenv
import os
import uvicorn
import time

load_dotenv()  # Load environment variables

# Create the FastAPI instance
app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


#)____________________________________________________NEW WEEK_______________________________________________________

def get_db_connection():
    return mysql.connector.connect(
        host="db", # because we are inside docker compose, we can use the service name as the host name
        user="root",
        password=os.getenv('MYSQL_ROOT_PASSWORD'),
        database=os.getenv('MYSQL_DATABASE')
    )
@app.get("/join")
async def get_join(request: Request):
    return templates.TemplateResponse("join.html", {"request": request})

@app.get("/api/joinFast")
async def get_fast():
    start_time = time.time()
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        query = """
        SELECT orders.order_id, customers.name AS customer_name, customers.email, products.name AS product_name, products.price, order_items.quantity, orders.order_date, orders.status
        FROM orders
        JOIN customers ON orders.customer_id = customers.customer_id
        JOIN order_items ON orders.order_id = order_items.order_id
        JOIN products ON order_items.product_id = products.product_id;
        """
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        connection.close()
        end_time = time.time()
        duration = end_time - start_time
        return {"data": result, "time_taken": duration}
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Error fetching orders on fast route")

@app.get("/api/joinSlow")
async def get_slow():
    start_time = time.time()
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)

        # Fetch all orders
        cursor.execute("SELECT * FROM orders;")
        orders = cursor.fetchall()

        # For each order, fetch corresponding customer and order item details, then product details for each order item
        for order in orders:
            cursor.execute("SELECT name AS customer_name, email FROM customers WHERE customer_id = %s;", (order['customer_id'],))
            customer = cursor.fetchone()
            order['customer_name'] = customer['customer_name']
            order['email'] = customer['email']

            cursor.execute("SELECT product_id, quantity FROM order_items WHERE order_id = %s;", (order['order_id'],))
            order_items = cursor.fetchall()

            products_details = []
            for item in order_items:
                cursor.execute("SELECT name AS product_name, price FROM products WHERE product_id = %s;", (item['product_id'],))
                product = cursor.fetchone()
                product['quantity'] = item['quantity']
                products_details.append(product)

            for products_detail in products_details:
                order['product_name'] = products_detail["product_name"]
                order['price'] = products_detail["price"]
                order['quantity'] = products_detail["quantity"]

        cursor.close()
        connection.close()
        end_time = time.time()
        duration = end_time - start_time
        return {"data": orders, "time_taken": duration}
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Error fetching orders on slow route")

@app.get("/api/challenge1")
async def challenge1():
    try:
        """
        Write a query to retrieve all customers and any orders they might have placed. 
        Include customers who haven't placed any orders. This demonstrates how to use a 
        LEFT JOIN to include all records from the 'left' table (customers) and matched records 
        from the 'right' table (orders), plus NULL in case of no match.
        """
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Error fetching total orders by customer")


@app.get("/api/challenge2")
async def challenge2():
    try:
        """
        -- Challenge: Write a GROUP BY query to calculate total revenue by category here
        """
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Error fetching total revenue by category")

#)____________________________________________________PREVIOUS WEEK_______________________________________________________

@app.get("/items", response_class=HTMLResponse)
async def get_items(request: Request):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM items")
    items = cursor.fetchall()
    cursor.close()
    conn.close()
    return templates.TemplateResponse("items.html", {"request": request, "items": items})

@app.get("/domdemo", response_class=HTMLResponse)
async def get_demo(request: Request):
    return templates.TemplateResponse("DOMManipulation.html", {"request": request})
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
async def read_notes(request: Request):
    """
    Read the notes from the file and return them.
    :return:
    """
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT note FROM notes ORDER BY `created_at` desc LIMIT 1")
        items = cursor.fetchone()
        print(items["note"])
        cursor.close()
        conn.close()
        return {"notes": items["note"]}
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