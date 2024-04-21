from fastapi import APIRouter, HTTPException, Depends
from app.services.doctor_service import DoctorService
from app.schemas.doctor_schema import Doctor, DoctorCreate, DoctorUpdate

doctor_router = APIRouter()
doctor_service = DoctorService()

@doctor_router.post("/", response_model=Doctor)
def create_doctor(doctor: DoctorCreate):

    return doctor_service.create_doctor(doctor)

@doctor_router.get("/", response_model=list[Doctor])
def get_doctor():

    return doctor_service.get_doctor()

@doctor_router.get("/{doctor_id}", response_model=Doctor)
def get_doctor(doctor_id: int):
    doctor = doctor_service.get_doctor_by_id(doctor_id)
    if doctor is None:
        raise HTTPException(status_code=404, detail="Doctor not found")
    
    return doctor

@doctor_router.put("/{doctor_id}", response_model=Doctor)
def update_doctor(doctor_id: int, doctor: DoctorUpdate):
    updated_doctor = doctor_service.update_doctor(doctor_id, doctor)
    if updated_doctor is None:
        raise HTTPException(status_code=404, detail="Doctor not found")
    
    return updated_doctor

@doctor_router.delete("/{doctor_id}", response_model=Doctor)
def delete_doctor(doctor_id: int):
    deleted_doctor = doctor_service.delete_doctor(doctor_id)
    if deleted_doctor is None:
        raise HTTPException(status_code=404, detail="Doctor not found")
    
    return deleted_doctor

@doctor_router.put("/{doctor_id}/set_doctor_availability/", response_model=Doctor)
def set_doctor_availability(doctor_id: int, is_available: bool):
    doctor = doctor_service.set_doctor_availability(doctor_id, is_available)
    if doctor is None:
        raise HTTPException(status_code=404, detail="Doctor not found")
    
    return doctor
