from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name:str
    description: str | None = None
    price:float
    tax:float | None = None


app = FastAPI()


@app.get("/")
async def root():
    return {"message":"hello world"}



@app.post("/user")
async def createUser(item:Item):
    item_dict = item.model_dump()
    if item.price is not None:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax":price_with_tax})
    return item_dict