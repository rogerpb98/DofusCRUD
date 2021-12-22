from pydantic import BaseModel

class Item(BaseModel):
    quantity: str
    name: str

class Almanax(BaseModel):
    date: str
    url: str
    bonus: str
    quest: str
    item: Item
    categories: list = []
