from fastapi import APIRouter, HTTPException, Depends
from app.services.appointment_service import AppointmentService
from app.schemas.appointment_schema import Appointment, AppointmentCreate, AppointmentUpdate

appointment_router = APIRouter()
appointment_service = AppointmentService()

@appointment_router.post("/", response_model=Appointment)
def create_appointment(appointment: AppointmentCreate):
    available_doctors = []

    return appointment_service.create_appointment(appointment, available_doctors)

@appointment_router.get("/", response_model=list[Appointment])
def get_appointments():

    return appointment_service.get_appointments()

@appointment_router.get("/{appointment_id}", response_model=Appointment)
def get_appointment(appointment_id: int):
    appointment = appointment_service.get_appointment_by_id(appointment_id)
    if appointment is None:
        raise HTTPException(status_code=404, detail="Appointment not found")
    
    return appointment

@appointment_router.put("/{appointment_id}", response_model=Appointment)
def update_appointment(appointment_id: int, appointment: AppointmentUpdate):
    updated_appointment = appointment_service.update_appointment(appointment_id, appointment)
    if updated_appointment is None:
        raise HTTPException(status_code=404, detail="Appointment not found")
    
    return updated_appointment

@appointment_router.delete("/{appointment_id}", response_model=Appointment)
def delete_appointment(appointment_id: int):
    deleted_appointment = appointment_service.delete_by_id(appointment_id)
    if deleted_appointment is None:
        raise HTTPException(status_code=404, detail="Appointment not found")
    
    return deleted_appointment