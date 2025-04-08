from .base_expert import BaseExpert

class ExpertRegistry:
    def __init__(self):
        self.experts = []

    def register(self, expert: BaseExpert):
        self.experts.append(expert)

    def get_candidates(self, input_text: str):
        return [e for e in self.experts if e.can_handle(input_text)]