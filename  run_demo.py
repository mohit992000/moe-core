from moe_core.router import MoERouter
from moe_core.registry import ExpertRegistry
from experts.code_expert import CodeExpert
from experts.resume_expert import ResumeExpert

if __name__ == "__main__":
    registry = ExpertRegistry()
    registry.register(CodeExpert())
    registry.register(ResumeExpert())

    router = MoERouter(registry)

    inputs = [
        "Can you help me improve my resume?",
        "Fix this function in my Python code.",
        "What's the weather like today?"
    ]

    for text in inputs:
        print(f"Input: {text}")
        print(f"Response: {router.route(text)}\n")