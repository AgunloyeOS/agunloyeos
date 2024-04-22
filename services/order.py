from fastapi import HTTPException

from schema.product import Product, products
from schema.order import OrderCreate

class OrderService:

    @staticmethod
    def order_parser(orders):

        for order in orders:
            order_items = order.items
            new_order = []
            for product_id in order_items:
                product = products.get(product_id)
                new_order.append(product)
            order.items = new_order
        return orders
    
    def checkout_order(self, orders: list[Order], order_id: int):
        for order in orders:
            if order.id == order_id:
                order.status = OrderStatus.completed
                return order
            
            raise ValueError("Order not found")

    @staticmethod
    def check_availability(payload: OrderCreate):
        product_ids = payload.items
        for product_id in product_ids:
            product: Product = products.get(int(product_id))
            if product.quantity_available < 1:
                raise HTTPException(status_code=400, detail='Product is unavailable')
            product.quantity_available -= 1
        return payload
    
    
            
        
    
order_service = OrderService()