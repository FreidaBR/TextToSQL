from utils.gemini import ask_gemini


class AnalystAgent:

    def run(self, context):

        # Handle failed execution
        if context.results is None:

            context.analysis = (
                "The SQL query could not be executed successfully even after "
                "automatic recovery. Please review the generated SQL or verify "
                "the database schema."
            )

            context.logs.append({
                "agent": "Analyst",
                "status": "Failed",
                "message": "No results available for analysis."
            })

            return context

        prompt = f"""
You are a Business Data Analyst.

Question:
{context.user_query}

SQL:
{context.validated_sql}

Results:
{context.results.to_string(index=False)}

Provide:

1. Summary
2. Key Insight
3. Recommendation

Keep the response under 150 words.
"""

        context.analysis = ask_gemini(prompt)

        context.logs.append({
            "agent": "Analyst",
            "status": "Completed",
            "message": "Generated business insights."
        })

        return context