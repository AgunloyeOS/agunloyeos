from schema.customer import Customer

class CustomerService:

    def create_customer(self, customers: list[Customer], customer_email: str, new_customer):
        for customer in customers:  
            if customer.email == customer_email:
                raise ValueError("Email already exists")
        
        new_customer.id = len(customers) + 1
        customers.append(new_customer)
        
        return new_customer
    
    def get_customer(self, customers: list[Customer]):

        return customers

    def get_customer_by_id(self, customers: list[Customer], customer_id: int):
        for customer in customers:
            if customer.id == customer_id:
                return customer
            
        return None
    
    def get_customer_by_email(self, customers: list[Customer], customer_email: str):
        for customer in customers:
            if customer.email == customer_email:
                return customer
            
        return None

    def edit_customer(self, customers: list[Customer], customer_id: int, edited_customer):
        for customer in customers:
            if customer.id == customer_id:
                for key, value in edited_customer.dict().items():
                    setattr(customer, key, value)
                return customer
            
        return None

    def delete_customer(self, customers: list[Customer], customer_id: int):
        for index, doctor in enumerate(customers):
            if doctor.id == customer_id:
                deleted_customer = customers.pop(index)
                return deleted_customer
            
        return None

    
