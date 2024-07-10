from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
from starlette.responses import FileResponse
import requests
import os
app = FastAPI()

templates = Jinja2Templates(directory="static")


@app.get("/")
def home():
    return FileResponse("static/home.html")


@app.post("/add_product")
def add_product(request: Request, product_name: str = Form(...), price: int = Form(...), category: str = Form(...)):
    data = {"name": product_name, "price": price, "productCategory": category}
    response = requests.post(os.environ["db_url"], json=data)
    if response.status_code == 200:
        return {"message": "Product added successfully and sent to other API"}
    else:
        return {"message": "Error sending data to other API"}
    

@app.get("/add_product")
def get_product():
    return FileResponse("static/add_product.html")
