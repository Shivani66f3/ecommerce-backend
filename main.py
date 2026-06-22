from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Backend running"}

@app.get("/products")
def get_products():
    return [
        {
            "id": 1,
            "name": "Wireless Headphones",
            "price": 2999,
            "image": "https://via.placeholder.com/200"
        },
        {
            "id": 2,
            "name": "Smart Watch",
            "price": 4999,
            "image": "https://via.placeholder.com/200"
        },
        {
            "id": 3,
            "name": "Laptop Bag",
            "price": 1499,
            "image": "https://via.placeholder.com/200"
        }
    ]
