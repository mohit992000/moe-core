from moe_core.registry import ExpertRegistry

class MoERouter:
    def __init__(self, registry: ExpertRegistry):
        self.registry = registry

    def route(self, input_text: str) -> str:
        candidates = self.registry.get_candidates(input_text)
        if not candidates:
            return "No expert available to handle the input."
        return candidates[0].infer(input_text)