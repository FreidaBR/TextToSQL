from orchestrator import SQLSenseOrchestrator

agent = SQLSenseOrchestrator()

context = agent.run(
    "Show top 5 products by sales"
)

print(context.intent)

print()

print(context.full_schema)