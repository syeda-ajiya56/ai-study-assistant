# AI Study Assistant

A mini Generative AI application that helps students understand educational topics through clear explanations, key points, examples, and practice questions.

## Problem

Students often need quick, simple explanations of difficult concepts while studying. This application provides structured AI-generated study help in a consistent format.

## Target Users

- School and university students
- Beginners learning technical or academic concepts
- Learners who want quick explanations and practice questions

## Main Feature

The AI Study Assistant accepts a student's question and generates a structured study response containing:

- **Topic**
- **Simple explanation**
- **3 key points**
- **1 example**
- **2 practice questions**
- **Safety/reliability note** when information is unavailable or uncertain

## AI Model

- **API:** Google Gemini API
- **Model:** `gemini-flash-latest`
- **Language:** Python

## Generative AI Concepts Used

### 1. LLM API Integration

The application connects to the Gemini API to generate responses to student questions.

### 2. Prompt Engineering

A system prompt defines the assistant's role, response format, educational style, and reliability rules.

### 3. Structured Output

The Gemini response is requested as JSON using:

```python
response_mime_type = "application/json"
```

This makes the output easier for the application to parse and display consistently.

### 4. Evaluation and Guardrails

The application was tested with normal questions, invalid input, and unavailable/future information.

The prompt instructs the AI not to invent facts and to provide a safe fallback when reliable information is unavailable.

## Useful Feature Beyond Basic Generation

Instead of returning only a paragraph, the application automatically creates a mini study package:

1. Explanation
2. Key points
3. Example
4. Practice questions
5. Reliability note

## Architecture

```text
Student Question
       |
       v
Python CLI Application
       |
       v
Prompt + Reliability Rules
       |
       v
Gemini API
       |
       v
Structured JSON Response
       |
       v
Validation / Safe Fallback
       |
       v
Study Response Displayed
```

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/syeda-ajiya56/ai-study-assistant.git
cd ai-study-assistant
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate the Environment

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

```bash
pip install google-genai python-dotenv
```

### 5. Create `.env`

Create a `.env` file in the project root:

```text
GEMINI_API_KEY=your_api_key_here
```

> **Important:** Never commit your `.env` file or expose your API key publicly.

### 6. Run the Application

```bash
python main.py
```

Type `exit` to quit.

## Example

### Example Input

```text
Explain recursion in simple terms for a beginner.
```

The application returns a structured response with an explanation, key points, an example, practice questions, and a reliability note.

## Evaluation and Testing

The application was tested with multiple types of inputs:

| Test | Input | Result |
|---|---|---|
| 1 | Explain recursion in simple terms | Structured educational response |
| 2 | Explain object-oriented programming in Java | Structured educational response |
| 3 | `asdfgh123` | Safe handling of unclear input |
| 4 | What exact questions will be on my university exam tomorrow? | Safe fallback for unavailable/future information |
| 5 | Explain photosynthesis for a school student | Structured educational response |
| 6 | What is 2 + 2? | Correct structured response |

## Reliability Improvement

An initial test showed that an unsupported/future-information question could cause the response to be returned in an unreliable format.

The application was improved by adding structured JSON output using:

```python
"response_mime_type": "application/json"
```

The prompt was also strengthened with reliability rules requiring the assistant to avoid invented information and clearly state when reliable information is unavailable.

### Before

The response could contain incorrectly nested JSON or plain text, causing the application to fail JSON parsing.

### After

The same unavailable-information question produced a clean structured response with a safe fallback such as:

```text
I don't have enough reliable information to answer that.
```

This made the application more predictable and reliable.

## Limitations

- The application depends on access to the Gemini API.
- AI-generated explanations may still contain mistakes.
- The application does not access private university records or future exam papers.
- It does not use a private course database or external knowledge base.
- The current version is a command-line application rather than a web interface.

## AI Work Disclosure

Generative AI tools were used during development for brainstorming, implementation guidance, debugging support, prompt design, and documentation assistance. The final application was tested locally, and the implementation was reviewed and adjusted to meet the project requirements.

## License

This project was created as part of a Generative AI learning/internship project.
