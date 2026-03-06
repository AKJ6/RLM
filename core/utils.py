import re

def extract_code(text):

    pattern = r"```(?:python)?\s*(.*?)```"

    match = re.search(pattern, text, re.DOTALL)

    if match:
        code = match.group(1).strip()

        # remove accidental leading "python"
        if code.startswith("python"):
            code = code[len("python"):].strip()

        return code

    return None