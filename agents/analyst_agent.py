from utils.gemini import ask_gemini


class AnalystAgent:

    def run(self, context):

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

Keep it under 150 words.
"""

        context.analysis = ask_gemini(prompt)

        context.logs.append({
            "agent": "Analyst",
            "status": "Completed",
            "message": "Generated insights."
        })

        return context