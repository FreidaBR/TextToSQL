from utils.validator import validate
from utils.gemini import ask_gemini


class CriticAgent:

    def run(self, context):

        if validate(context.generated_sql):

            context.validated_sql = context.generated_sql

            context.logs.append({
                "agent": "Critic",
                "status": "Passed",
                "message": "SQL validated."
            })

            return context

        prompt = f"""
Fix this SQL.

Return ONLY corrected SQL.

{context.generated_sql}
"""

        fixed = ask_gemini(prompt)

        fixed = (
            fixed.replace("```sql", "")
            .replace("```", "")
            .strip()
        )

        context.validated_sql = fixed

        context.logs.append({
            "agent": "Critic",
            "status": "Corrected",
            "message": "Unsafe SQL corrected."
        })

        return context