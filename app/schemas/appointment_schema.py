from pydantic import BaseModel


class Appointment(BaseModel):
    id: int
    patient: int
    doctor: int
    date: str

class AppointmentCreate(BaseModel):
    patient: int
    date: str

class AppointmentUpdate(BaseModel):
    patient: int
    doctor: int
    date: str