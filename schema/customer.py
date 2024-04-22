from pydantic import BaseModel, EmailStr

class Customer(BaseModel):
    id: int
    email: EmailStr
    name: str
    password: str

class CustomerCreate(BaseModel):
    email: EmailStr
    name: str
    password: str

class CustomerEdit(CustomerCreate):
    pass


customers: list[Customer] = [
    Customer(id=1, username="damilare", address="3, olusola str"),
    Customer(id=2, username="sweetboy", address="23, johnson str")
]