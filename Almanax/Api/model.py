#!/usr/bin/python
# coding=utf-8

from typing import Any
from pydantic import BaseModel

class Item(BaseModel):
    quantity: str
    name: str

class Almanax(BaseModel):
    date: Any
    url: str
    bonus: str
    quest: str
    item: Item
    categories: list = []
