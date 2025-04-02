class ResourceNotFound(Exception):
    def __init__(self, resource_id):
        self.message = f"Resource not found. Id {resource_id}"
        super().__init__(self.message)
        self.resource_id = resource_id
        self.status_code = 404

    def to_dict(self):
        return {
            'message': self.message,
            'resource_id': self.resource_id
        }