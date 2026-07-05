from utils.gemini import ask_gemini


class SQLAgent:

    def run(self, context):

        prompt = f"""
You are an expert SQLite developer.

User Question:
{context.user_query}

Intent:
{context.intent}

Relevant Tables:
{context.selected_schema}

Database Schema:
{context.full_schema}

Generate ONLY a valid SQLite SQL query.

Rules:
- Return SQL only
- No markdown
- No explanation
- SELECT queries only
"""

        sql = ask_gemini(prompt)

        sql = (
            sql.replace("```sql", "")
            .replace("```", "")
            .strip()
        )

        context.generated_sql = sql

        context.logs.append({
            "agent": "SQL Agent",
            "status": "Completed",
            "message": "SQL generated."
        })

        return context