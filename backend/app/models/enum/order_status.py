from enum import Enum

class OrderStatus(Enum):
    WAITING_PAYMENT = 7
    PAID = 6
    PENDING = 1
    PROCESSING = 2
    SHIPPED = 3
    DELIVERED = 4
    CANCELLED = 5

    def __str__(self):
        return self.name