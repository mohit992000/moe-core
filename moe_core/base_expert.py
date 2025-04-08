class BaseExpert:
    def __init__(self, name):
        self.name = name

    def can_handle(self, input_text: str) -> bool:
        """Determine if this expert can handle the given input."""
        raise NotImplementedError

    def infer(self, input_text: str) -> str:
        """Perform inference with this expert."""
        raise NotImplementedError
    