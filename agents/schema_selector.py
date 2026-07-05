from utils.gemini import ask_gemini
from utils.parser import extract_json


class SchemaSelector:

    def run(self, context):

        prompt = f"""
You are a Database Expert.

Below is the user's intent.

{context.intent}

Below is the database schema.

{context.full_schema}

Choose ONLY the tables required.

Return ONLY JSON.

Format:

{{
    "tables": [],
    "reason":""
}}

Do not explain anything else.
"""

        response = ask_gemini(prompt)

        result = extract_json(response)

        context.selected_schema = result

        context.logs.append({
            "agent": "Schema Selector",
            "status": "Completed",
            "message": result["reason"]
        })

        return context