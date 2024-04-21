from fastapi import FastAPI
from app.routers.appointment import  appointment_router
from app.routers.doctors import  doctor_router
from app.routers.patient import patient_router

app = FastAPI()

app.include_router(patient_router, prefix="/api", tags=["Patients"])
app.include_router(doctor_router, prefix="/api", tags=["Doctors"])
app.include_router(appointment_router, prefix="/api", tags=["Appointments"])

@app.get("/")
def home():
    return "Welcome to Life First Hospital" 