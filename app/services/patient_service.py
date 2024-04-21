from app.schemas.patient_schema import Patient


class PatientService:
     
     def create_patient(self, patients: list[Patient], new_patient):
       
        new_patient.id = len(patients) + 1
        patients.append(new_patient)

        return new_patient
 

     def get_patient(self, patients: list[Patient]):

        return patients

     def get_patient_by_id(self, patients: list[Patient], patient_id: int):
        for patient in patients:
            if patient.id == patient_id:
                return patient
            
        return None

     def update_patient(self, patients: list[Patient], patient_id: int, updated_patient):
        for patient in patients:
            if patient.id == patient_id:
                for key, value in updated_patient.dict().items():
                    setattr(patient, key, value)
                return patient
            
        return None

     def delete_patient(self, patients: list[Patient], patient_id: int):
        for index, patient in enumerate(patients):
            if patient.id == patient_id:
                deleted_patient = patients.pop(index)
                return deleted_patient
            
        return None
     
     

     