# backend/llm_engine.py
from .utils import get_meaningful_code_files

def analyze_code_with_llm(repo_path: str):
    import ollama   # import inside to avoid loading model metadata at start of app 

    files = get_meaningful_code_files(repo_path)
    if not files:
        return ["No meaningful code files found in the repository."]

    all_code = "\n\n".join(f["content"] for f in files)

    prompt = f"""
You are a senior AI technical interviewer reviewing a software codebase. Your goal is to generate 5 deep, intelligent, and relevant interview questions that help assess a candidate’s understanding of this specific codebase.

Instructions:
- Focus only on what can be inferred from the actual code content provided.
- Ask questions that explore the architecture, implementation choices, edge cases, potential bugs, logic design, or trade-offs.
- Avoid generic questions. Be specific and relevant to the content.
- Prefer asking about patterns, decisions, or interdependencies visible in the code.
- Do NOT ask about files, tools, or technologies that are not shown or clearly used in the code.

Here is a partial view of the codebase (first 5000 characters):

{all_code[:5000]}

Generate exactly 5 smart, specific, and relevant interview questions:
"""

    response = ollama.chat(
        model="qwen2.5vl:7b",
        messages=[{"role": "user", "content": prompt}]
    )

    answer = response['message']['content']
    questions = [q.strip("-•. ").strip() for q in answer.split('\n') if q.strip()]
    return questions


