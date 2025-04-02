class DatabaseError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
        self.status_code = 400

    def to_dict(self):
        return {
            'message': self.message
        }