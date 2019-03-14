from .base_controller import BaseController


class BlueController(BaseController):
    def __init__(self):
        super().__init__()

    def get(self):
        return "blue"
