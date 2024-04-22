from pydantic import BaseModel
from enum import Enum
from schema.product import Product

class OrderStatus(Enum):
    pending = "pending"
    completed = "completed"

class Order(BaseModel):
    id: int
    customer_id: int
    items: list[int | Product]
    status: OrderStatus = OrderStatus.pending

class OrderCreate(BaseModel):
    customer_id: int
    items: list[int]

orders = [
    Order(id=1, customer_id=1, items=[1, 2])
]