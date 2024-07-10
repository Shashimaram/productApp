from fastapi import FastAPI, Query
from pydantic import BaseModel
import logging
import openai
import psycopg2
import os

app = FastAPI()

class Productdata(BaseModel):
    name: str
    price: int
    productCategory: str

def create_product(name, price, product_category, description):
    conn = psycopg2.connect(user=os.environ["dbUsername"], password=os.environ["dbPassword"], host=os.environ["dbHost"], port=5432, database=os.environ["dbDatabase"])
    cur = conn.cursor()
    cur.execute("INSERT INTO products (name, price, product_category, description) VALUES (%s, %s, %s, %s)",
                (name, price, product_category, description))
    conn.commit()
    cur.close()
    conn.close()

def generatingDescription(productName, productCategory, productPrice):
    system_content = f"generate a normal product description at{productName} at price of {productCategory} comes under category of {productPrice}?, please Please limit the responce to 20 words "
    user_content = "please write the description in 20 words."
    client = openai.OpenAI(
        api_key="b48d296ffce8438aa0f03bab4f3ab5ec",
        base_url="https://api.aimlapi.com",
    )
    chat_completion = client.chat.completions.create(
        model="mistralai/Mistral-7B-Instruct-v0.2",
        messages=[
            {"role": "system", "content": system_content},
            {"role": "user", "content": user_content},
        ],
        temperature=0.7,
        max_tokens=128,
    )
    response = chat_completion.choices[0].message.content  
    return response

@app.post("/")
def root(data: Productdata):
    logging.info("this is produce")
    print("i am triggred sucessfully")
    description = generatingDescription(data.name, data.productCategory, data.price)
    create_product(data.name,data.price,data.productCategory,description)
    return {"message": "Done"}


@app.post("/health")
def health():
    return 



@app.post("/test")
def health():
    return {"message":"testSuccessfull "}