from moe_core.base_expert import BaseExpert

class CodeExpert(BaseExpert):
    def __init__(self):
        super().__init__("CodeExpert")

    def can_handle(self, input_text: str) -> bool:
        return "code" in input_text.lower() or "function" in input_text.lower()

    def infer(self, input_text: str) -> str:
        return "Here's a suggestion for your code: [dummy output]"
    