from app.schemas.appointment_schema import Appointment

class AppointmentService:
    def create_appointment(self, appointments: list[Appointment], new_appointment):
        new_appointment.id = len(appointments) + 1
        appointments.append(new_appointment)
        
        return new_appointment
    
    def get_appointments(self, appointments: list[Appointment]):

        return appointments

    def get_appointment_by_id(self, appointments: list[Appointment], appointment_id: int):
        for appointment in appointments:
            if appointment.id == appointment_id:
                return appointment
            
        return None


    def update_appointment(self, appointments: list[Appointment], appointment_id: int, updated_appointment):
        for appointment in appointments:
            if appointment.id == appointment_id:
                for key, value in updated_appointment.dict().items():
                    setattr(appointment, key, value)
                return appointment
        return None

    def delete_appointment(self, appointments: list[Appointment], appointment_id: int):
        for index, appointment in enumerate(appointments):
            if appointment.id == appointment_id:
                deleted_appointment = appointments.pop(index)
                return deleted_appointment
            
        return None

    