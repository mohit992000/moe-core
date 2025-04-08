from moe_core.base_expert import BaseExpert

class ResumeExpert(BaseExpert):
    def __init__(self):
        super().__init__("ResumeExpert")

    def can_handle(self, input_text: str) -> bool:
        return "resume" in input_text.lower() or "cv" in input_text.lower()

    def infer(self, input_text: str) -> str:
        return "Here's how you can improve your resume: [dummy output]"