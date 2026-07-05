from utils.context import AgentContext

from agents.intent_agent import IntentAgent
from utils.schema_reader import SchemaReader
from agents.schema_selector import SchemaSelector
from agents.sql_agent import SQLAgent
from agents.critic_agent import CriticAgent
from agents.analyst_agent import AnalystAgent

from utils.executor import SQLExecutor


class SQLSenseOrchestrator:

    def __init__(self):

        self.intent = IntentAgent()
        self.reader = SchemaReader()
        self.selector = SchemaSelector()
        self.sql = SQLAgent()
        self.critic = CriticAgent()
        self.executor = SQLExecutor()
        self.analyst = AnalystAgent()

    def run(self, question):

        context = AgentContext()

        context.user_query = question

        context = self.intent.run(context)

        context.full_schema = self.reader.read_schema()

        context = self.selector.run(context)

        context = self.sql.run(context)

        context = self.critic.run(context)

        context.results = self.executor.execute(
            context.validated_sql
        )

        context = self.analyst.run(context)

        return context