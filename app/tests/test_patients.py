from fastapi.testclient import TestClient
from main import app
from app.schemas.patient_schema import PatientCreate, PatientUpdate
from app.services.patient_service import PatientService

client = TestClient(app)
patient_service = PatientService()

def test_create_patient():
    patient_data = {
        "name": "Tope",
        "age": 25,
        "sex": "Female",
        "weight": 52,
        "height": 170,
        "phone": "09034567860"
        }
    response = client.post("/patients/", json=patient_data)
    assert response.status_code == 200
    assert response.json()["name"] == "Tope"
    assert response.json()["age"] == 25

def test_read_patients():
    response = client.get("/patients/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_read_patient():
    patient_id = 1
    response = client.get(f"/patients/{patient_id}")
    assert response.status_code == 200
    assert response.json()["id"] == patient_id

def test_update_patient():
    patient_id = 1
    updated_data = {
        "phone": "09034567860"
    }
    response = client.put(f"/patients/{patient_id}", json=updated_data)
    assert response.status_code == 200
    assert response.json()["phone"] == "09034567860"

def test_delete_patient():
    patient_id = 1
    response = client.delete(f"/patients/{patient_id}")
    assert response.status_code == 200
    assert response.json()["id"] == patient_id