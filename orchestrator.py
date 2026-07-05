from utils.context import AgentContext

from agents.intent_agent import IntentAgent
from utils.schema_reader import SchemaReader
from agents.schema_selector import SchemaSelector
from agents.sql_agent import SQLAgent
from agents.critic_agent import CriticAgent
from agents.recovery_agent import RecoveryAgent
from agents.analyst_agent import AnalystAgent

from utils.executor import SQLExecutor


class SQLSenseOrchestrator:

    def __init__(self):

        self.intent = IntentAgent()
        self.reader = SchemaReader()
        self.selector = SchemaSelector()
        self.sql = SQLAgent()
        self.critic = CriticAgent()
        self.recovery = RecoveryAgent()
        self.executor = SQLExecutor()
        self.analyst = AnalystAgent()

    def run(self, question):

        # Create context
        context = AgentContext()

        context.user_query = question

        # Step 1 - Extract Intent
        context = self.intent.run(context)

        # Step 2 - Read Database Schema
        context.full_schema = self.reader.read_schema()

        # Step 3 - Select Relevant Tables
        context = self.selector.run(context)

        # Step 4 - Generate SQL
        context = self.sql.run(context)

        # Step 5 - Validate SQL
        context = self.critic.run(context)

        # Step 6 - Execute SQL with automatic retry
        while context.retry_count <= context.max_retries:

            try:

                context.results = self.executor.execute(
                    context.validated_sql
                )

                context.logs.append({
                    "agent": "SQL Executor",
                    "status": "Completed",
                    "message": "SQL executed successfully."
                })

                break

            except Exception as e:

                context.execution_error = str(e)

                context.logs.append({
                    "agent": "SQL Executor",
                    "status": "Failed",
                    "message": str(e)
                })

                # Stop if retry limit reached
                if context.retry_count >= context.max_retries:

                    context.logs.append({
                        "agent": "Recovery Agent",
                        "status": "Failed",
                        "message": "Maximum retry attempts reached."
                    })

                    context.results = None

                    break

                # Retry once
                context.retry_count += 1

                context = self.recovery.run(context)

        # Step 7 - Generate Analysis
        context = self.analyst.run(context)

        return context