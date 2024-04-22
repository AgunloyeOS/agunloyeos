from schema.product import Product

class ProductService:

    def create_product(self, products: list[Product], new_product):
        
        new_product.id = len(products) + 1
        products.append(new_product)
        
        return new_product
    
    def get_product(self, products: list[Product]):

        return products

    def get_product_by_id(self, products: list[Product], product_id: int):
        for product in products:
            if product_id.id == product_id:
                return product
            
        return None

    def edit_doctor(self, products: list[Product], product_id: int, edited_product):
        for product in products:
            if product.id == product_id:
                for key, value in edited_product.dict().items():
                    setattr(product, key, value)
                return product
            
        return None

    def delete_product(self, products: list[Product], product_id: int):
        for index, product in enumerate(products):
            if products.id == product_id:
                deleted_product = products.pop(index)
                return deleted_product
        return None