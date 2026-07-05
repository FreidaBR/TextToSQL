from orchestrator import SQLSenseOrchestrator
from agents.schema_selector import SchemaSelector

agent = SQLSenseOrchestrator()

context = agent.run(
    "Show top 5 products by sales"
)

selector = SchemaSelector()

context = selector.run(context)

print(context.selected_schema)