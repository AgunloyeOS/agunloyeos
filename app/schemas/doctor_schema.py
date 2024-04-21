from pydantic import BaseModel


class Doctor(BaseModel):
    id: int
    name: str
    specialization: str
    phone: str
    is_available: bool = True


class DoctorCreate(BaseModel):
    name: str
    specialization: str
    phone: str

class DoctorUpdate(DoctorCreate):
    name: str
    specialization: str
    phone: str
    is_available: bool

#      OR
#class PatientUpdate(BaseModel):
#     name: str
#     specialization: str
#     phone: str
#     is_available: bool = True