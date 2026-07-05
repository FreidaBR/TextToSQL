from utils.context import AgentContext
from agents.intent_agent import IntentAgent

context = AgentContext()

context.user_query = "Show the top 5 products by sales."

agent = IntentAgent()

context = agent.run(context)

print(context.intent)