import google.generativeai as genai
from typing import List

# Set your API key
genai.configure(api_key="AIzaSyAO6GWzefLDXqr6RX9-tfpWdRSTE2D9Mf0")

# Load Gemini model (using Gemini Pro, you can change this if needed)
model = genai.GenerativeModel("models/gemini-1.5-flash")

# Template prompt
TEMPLATE = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully:\n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string (''). "
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)

# Function to parse using Gemini
def parse_with_gemini(dom_chunks: List[str], parse_description: str) -> str:
    parsed_results = []

    for i, chunk in enumerate(dom_chunks, start=1):
        prompt = TEMPLATE.format(dom_content=chunk, parse_description=parse_description)

        response = model.generate_content(prompt)

        content = response.text.strip() if response.text else ""
        print(f"Parsed batch: {i} of {len(dom_chunks)}")
        parsed_results.append(content)

    return "\n".join(parsed_results)
