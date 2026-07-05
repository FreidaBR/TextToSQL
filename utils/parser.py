import json
import re


def extract_json(response: str):
    """
    Extract JSON from Gemini responses.
    Handles markdown code blocks automatically.
    """

    cleaned = re.sub(r"```json|```", "", response).strip()

    return json.loads(cleaned)