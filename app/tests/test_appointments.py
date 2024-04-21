from fastapi.testclient import TestClient
from main import app
from app.schemas.appointment_schema import AppointmentCreate, AppointmentUpdate
from app.services.appointment_service import AppointmentService

client = TestClient(app)
appointment_service = AppointmentService()

def test_create_appointment():
    appointment_data = {
        "patient": 3,
        "doctor": 3,
        "date": "2023-07-01T09:00:00"
    }
    response = client.post("/appointments/", json=appointment_data)
    assert response.status_code == 200
    assert response.json()["patient"] == 1
    assert response.json()["doctor"] == 1
    assert response.json()["date"] == "2023-07-01T09:00:00"

def test_read_appointments():
    response = client.get("/appointments/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_read_appointment():
    appointment_id = 1
    response = client.get(f"/appointments/{appointment_id}")
    assert response.status_code == 200
    assert response.json()["id"] == appointment_id

def test_update_appointment():
    appointment_id = 1
    updated_data = {
        "date": "2024-05-02T11:00:00"
    }
    response = client.put(f"/appointments/{appointment_id}", json=updated_data)
    assert response.status_code == 200
    assert response.json()["date"] == "2024-05-02T11:00:00"

def test_delete_appointment():
    appointment_id = 1
    response = client.delete(f"/appointments/{appointment_id}")
    assert response.status_code == 200
    assert response.json()["id"] == appointment_id