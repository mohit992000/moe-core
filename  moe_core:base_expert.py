class BaseExpert:
    def __init__(self, name):
        self.name = name

    def can_handle(self, input_text: str) -> bool:
        raise NotImplementedError

    def infer(self, input_text: str) -> str:
        raise NotImplementedError