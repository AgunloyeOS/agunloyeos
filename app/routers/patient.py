from fastapi import APIRouter, HTTPException, Depends
from app.services.patient_service import PatientService
from app.schemas.patient_schema import Patient, PatientCreate, PatientUpdate

patient_router = APIRouter()
patient_service = PatientService()

@patient_router.post("/", response_model=Patient)
def create_patient(patient: PatientCreate):

    return patient_service.create_patient(patient)

@patient_router.get("/", response_model=list[Patient])
def get_patient():

    return patient_service.get_patient()

@patient_router.get("/{patient_id}", response_model=Patient)
def get_patient(patient_id: int):
    patient = patient_service.get_patient_by_id(patient_id)
    if patient:
          return {"message": "Patient found succesfully", "data": patient}
    else:
        raise HTTPException(status_code=404, detail="Patient not found")
   

@patient_router.put("/{patient_id}", response_model=Patient)
def update_patient(patient_id: int, patient: PatientUpdate):
    updated_patient = patient_service.update_patient(patient_id, patient)

    if updated_patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    
    return {"message": "update succesful", "data": updated_patient}
    
    # return updated_patient

@patient_router.delete("/{patient_id}", response_model=Patient)
def delete_patient(patient_id: int):
    deleted_patient = patient_service.delete_patient(patient_id)
    if deleted_patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    
    return {"message": "Sad to see you go", "data": deleted_patient}
    
    # return deleted_patient