import json
import re

from utils.gemini import ask_gemini


class IntentAgent:

    def run(self, context):

        prompt = f"""
You are an Intent Extraction Agent.

Your ONLY job is to understand the user's request.

Return ONLY valid JSON.

User Question:
{context.user_query}

Return this exact structure:

{{
    "goal":"",
    "metric":"",
    "filters":{{}},
    "group_by":"",
    "sort":"",
    "limit":0,
    "needs_clarification":false,
    "confidence":0.0
}}

Do not explain.
Do not use markdown.
Return JSON only.
"""

        response = ask_gemini(prompt)

        print("\n===== RAW GEMINI RESPONSE =====")
        print(response)
        print("===============================\n")

        try:
            # Remove markdown code fences
            cleaned = re.sub(r"```json|```", "", response).strip()

            context.intent = json.loads(cleaned)

        except Exception as e:

            print("JSON Parsing Error:", e)

            context.intent = {
                "goal": "Unknown",
                "needs_clarification": True,
                "confidence": 0
            }

        context.logs.append({
    "agent": "Intent Agent",
    "message": "Intent extracted successfully."
})

        return context