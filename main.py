import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is missing from the .env file.")

client = genai.Client(api_key=api_key)

SYSTEM_PROMPT = """
You are an AI Study Assistant for students.

Your job is to explain educational topics clearly and accurately.

Rules:
1. Use simple, student-friendly language.
2. Give a concise explanation.
3. Include 3 key points.
4. Include one simple example.
5. Give 2 practice questions.
6. Do not invent facts.
7. If the user asks for information you cannot reliably know, clearly say:
   "I don't have enough reliable information to answer that."
8. Never claim to know future exam questions, private information, or unavailable information.
9. Stay focused on educational help.

Return ONLY valid JSON with exactly these keys:
topic
explanation
key_points
example
practice_questions
safe_note
"""

def ask_study_assistant(question):
    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=f"""
{SYSTEM_PROMPT}

Student question:
{question}
""",
        config={
            "response_mime_type": "application/json"
        }
    )

    text = response.text.strip()

    try:
        # Remove accidental markdown code fences if the model adds them.
        if text.startswith("```"):
            text = text.replace("```json", "", 1)
            text = text.replace("```", "", 1).strip()

        return json.loads(text)

    except json.JSONDecodeError:
        return {
            "topic": question,
            "explanation": "I don't have enough reliable information to provide a structured answer.",
            "key_points": [],
            "example": "",
            "practice_questions": [],
            "safe_note": "The AI response could not be verified as structured JSON."
        }

print("\nAI Study Assistant")
print("=" * 50)
print("Ask a study question. Type 'exit' to quit.")

while True:
    question = input("\nYour question: ").strip()

    if question.lower() == "exit":
        print("\nGoodbye! Keep learning.")
        break

    if not question:
        print("Please enter a study question.")
        continue

    if len(question) > 500:
        print("Please keep your question under 500 characters.")
        continue

    result = ask_study_assistant(question)

    print("\n" + "-" * 50)
    print("TOPIC:", result.get("topic", ""))
    print("\nEXPLANATION:")
    print(result.get("explanation", ""))

    print("\nKEY POINTS:")
    for point in result.get("key_points", []):
        print("•", point)

    print("\nEXAMPLE:")
    print(result.get("example", ""))

    print("\nPRACTICE QUESTIONS:")
    for q in result.get("practice_questions", []):
        print("•", q)

    if result.get("safe_note"):
        print("\nNOTE:")
        print(result["safe_note"])

    print("-" * 50)