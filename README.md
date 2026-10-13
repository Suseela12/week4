# Experiment 4: Prompt Failure Diagnosis and Correction

## Aim
To identify common prompt failures, understand their causes, and improve prompts through systematic correction.

## Problem Statement
Evaluate three problematic prompts involving hallucination, format constraint violations, and over-refusal. Generate responses to original and corrected prompts using the same LLM.

## Technologies Used
- Python
- Google Gemini AI
- Google Gen AI SDK

## Failure Types

### 1. Hallucination
A model may invent an answer to a question based on a false assumption.

**Mitigation:** Ask the model to verify the premise and acknowledge uncertainty.

### 2. Instruction Ignoring
A model may fail to follow exact formatting instructions.

**Mitigation:** Specify the required number of lines, bullet structure, and restrictions on extra text.

### 3. Over-Refusal
A model may refuse a harmless educational request.

**Mitigation:** Clearly state the educational purpose and appropriate audience.

## Algorithm
1. Initialize the Gemini API client.
2. Define the original and corrected prompts.
3. Send each original prompt to the LLM.
4. Display the original response and suspected failure diagnosis.
5. Send the corrected prompt to the same LLM.
6. Display the improved response.
7. Summarize the lessons learned.
8. Save all results to a text file.

## Installation

```bash
pip install -r requirements.txt
```

## Configuration
Set the `GEMINI_API_KEY` environment variable before running the program. Never upload API keys to GitHub.

## Execution

```bash
python src/main.py
```

## Expected Output
- Original prompt and response.
- Failure type and suspected root cause.
- Corrected prompt and response.
- Final summary of prompt improvement techniques.
- Saved results in `output/diagnosis_results.txt`.

## Result
The experiment demonstrates how clearer instructions and premise verification can help reduce hallucination risk, improve formatting compliance, and avoid unnecessary refusals.

## Conclusion
Systematic prompt diagnosis helps identify weaknesses in LLM interactions. Corrected prompts can improve response quality, but their effectiveness must be verified against actual model outputs.
