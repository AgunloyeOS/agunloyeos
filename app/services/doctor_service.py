from app.schemas.doctor_schema import Doctor

class DoctorService:

    def create_doctor(self, doctors: list[Doctor], new_doctor):
        
        new_doctor.id = len(doctors) + 1
        doctors.append(new_doctor)
        
        return new_doctor
    
    def get_doctor(self, doctors: list[Doctor]):
        return doctors

    def get_doctor_by_id(self, doctors: list[Doctor], doctor_id: int):
        for doctor in doctors:
            if doctor.id == doctor_id:
                return doctor
        return None

    def update_doctor(self, doctors: list[Doctor], doctor_id: int, updated_doctor):
        for doctor in doctors:
            if doctor.id == doctor_id:
                for key, value in updated_doctor.dict().items():
                    setattr(doctor, key, value)
                return doctor
        return None

    def delete_doctor(self, doctors: list[Doctor], doctor_id: int):
        for index, doctor in enumerate(doctors):
            if doctor.id == doctor_id:
                deleted_doctor = doctors.pop(index)
                return deleted_doctor
        return None

    def set_doctor_availability(self, doctors: list[Doctor], doctor_id: int, is_available: bool):
        for doctor in doctors:

          if doctor.id == doctor_id:
            doctor.is_available = is_available
            return doctor
        
        return None
