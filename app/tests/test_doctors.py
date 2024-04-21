from fastapi.testclient import TestClient
from main import app
from app.schemas.doctor_schema import DoctorCreate, DoctorUpdate
from app.services.doctor_service import DoctorService

client = TestClient(app)
doctor_service = DoctorService()

def test_create_doctor():
    doctor_data = {
        "name": "Dr. John Doe",
        "specialization": "Gynaecologist",
        "phone": "07066428182"
    }
    response = client.post("/doctors/", json=doctor_data)
    assert response.status_code == 200
    assert response.json()["name"] == "Dr. John Doe"
    assert response.json()["specialization"] == "Gynaecologist"

def test_read_doctors():
    response = client.get("/doctors/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_read_doctor():
    doctor_id = 1
    response = client.get(f"/doctors/{doctor_id}")
    assert response.status_code == 200
    assert response.json()["id"] == doctor_id

def test_update_doctor():
    doctor_id = 1
    updated_data = {
        "phone": "0987654321"
    }
    response = client.put(f"/doctors/{doctor_id}", json=updated_data)
    assert response.status_code == 200
    assert response.json()["phone"] == "07066429234"

def test_delete_doctor():
    doctor_id = 1
    response = client.delete(f"/doctors/{doctor_id}")
    assert response.status_code == 200
    assert response.json()["id"] == doctor_id