from moe_core.router import MoERouter
from moe_core.registry import ExpertRegistry
from experts.code_expert import CodeExpert
from experts.resume_expert import ResumeExpert

print("✅ Starting MoE System...")

if __name__ == "__main__":
    print("✅ Inside main block")

    # Create the registry and register experts
    registry = ExpertRegistry()
    print("🧠 Registering CodeExpert...")
    registry.register(CodeExpert())
    print("🧠 Registering ResumeExpert...")
    registry.register(ResumeExpert())

    # Create router
    router = MoERouter(registry)
    print("🚦 MoE Router ready.")

    # Example input prompts
    inputs = [
        "Can you help me improve my resume?",
        "Fix this function in my Python code.",
        "What's the weather like today?"
    ]

    # Run each input through the router
    for text in inputs:
        print(f"\n🔍 Input: {text}")
        response = router.route(text)
        print(f"💬 Response: {response}")