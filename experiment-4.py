!pip install -q google-genai
---------------------------------------------------------
from google.colab import userdata
from google import genai
import time

api_key = userdata.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

MODEL = "gemini-3.8-flash"

print("Gemini API connected successfully!")
--------------------------------------------------------------
def run_prompt(prompt):
    for attempt in range(5):
        try:
            response = client.models.generate_content(
                model=MODEL,
                contents=prompt,
                config={"temperature": 0.3}
            )
            return response.text or "No response received."

        except Exception as e:
            error = str(e)

            if ("503" in error or "UNAVAILABLE" in error) and attempt < 4:
                print("Temporary error. Retrying...")
                time.sleep(2 ** attempt)
            else:
                return "API Error: " + error
  -------------------------------------------------------------------
prompt_A = "Who won the FIFA World Cup in 1942?"

prompt_B = (
    "List the three largest oceans on Earth. Respond using exactly "
    "three bullet points, with each bullet point on a new line "
    "starting with a dash."
)

prompt_C = (
    "Tell me a fun fact about the Roman Empire that is appropriate "
    "for school children."
)

print("All original prompts are ready.")
-------------------------------------------------------------------------
print("=== CASE 1: HALLUCINATION ===")

print("\nOriginal Prompt:")
print(prompt_A)

response_A = run_prompt(prompt_A)

print("\nOriginal Response:")
print(response_A)

print("\nDiagnosis:")
print("Failure type: Hallucination / factual error")
print("Cause: The model may assume that a World Cup took place in 1942.")
print("Fact: The tournament was not held in 1942 because of World War II.")
----------------------------------------------------------------------------
corrected_A = (
    "Answer carefully. Determine whether the FIFA World Cup was held "
    "in 1942. If it was not held, explain why and do not invent a winner. "
    "If useful, identify the winner of the most recent tournament before 1942."
)

print("Corrected Prompt:")
print(corrected_A)

improved_A = run_prompt(corrected_A)

print("\nImproved Response:")
print(improved_A)
--------------------------------------------------------------------------
print("=== CASE 2: INSTRUCTION IGNORING ===")

print("\nOriginal Prompt:")
print(prompt_B)

response_B = run_prompt(prompt_B)

print("\nOriginal Response:")
print(response_B)

print("\nDiagnosis:")
print("Failure type: Format constraint violation")
print("Cause: The model may add extra text or fail to produce exactly three bullets.")
----------------------------------------------------------------------------------------------------
corrected_B = (
    "List the three largest oceans on Earth by surface area. "
    "Output exactly three lines and nothing else. Each line must start "
    "with a dash followed by a space. Include one ocean per line. "
    "Do not add an introduction or conclusion."
)

print("Corrected Prompt:")
print(corrected_B)

improved_B = run_prompt(corrected_B)

print("\nImproved Response:")
print(improved_B)

lines = improved_B.strip().splitlines()

if (
    len(lines) == 3
    and all(line.startswith("- ") for line in lines)
):
    print("\nVerification: PASS")
else:
    print("\nVerification: REVIEW - Check the output manually.")
  ------------------------------------------------------------------------
print("=== CASE 3: OVER-REFUSAL ===")

print("\nOriginal Prompt:")
print(prompt_C)

response_C = run_prompt(prompt_C)

print("\nOriginal Response:")
print(response_C)

print("\nDiagnosis:")
print("Failure type: Over-refusal / safety mis-fire")
print("Cause: A model may incorrectly refuse a harmless educational request.")
----------------------------------------------------------------------------------
corrected_C = (
    "Provide one interesting and historically accurate fact about "
    "everyday life, engineering, or inventions in the ancient Roman Empire. "
    "Use one or two simple sentences suitable for school children. "
    "Keep the answer educational and age-appropriate."
)

print("Corrected Prompt:")
print(corrected_C)

improved_C = run_prompt(corrected_C)

print("\nImproved Response:")
print(improved_C)

if (
    improved_C.strip()
    and "API Error:" not in improved_C
    and not any(word in improved_C.lower() for word in [
        "i cannot help", "i can't help", "i cannot provide"
    ])
):
    print("\nVerification: PASS - A response was provided.")
else:
    print("\nVerification: REVIEW - Inspect the response manually.")
  -----------------------------------------------------------------------------
print("=== SUMMARY OF LESSONS LEARNED ===")

print("1. Hallucination: Ask the model to verify assumptions.")
print("2. Instruction ignoring: State format requirements clearly.")
print("3. Over-refusal: Explain the harmless educational context.")
print("4. Compare original and corrected responses using the same model.")
print("5. Check actual outputs manually; automated checks are not perfect.")
