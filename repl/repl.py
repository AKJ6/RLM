import sys
import os
import logging

sys.path.append(".")

from core.llm import LocalLLM
from core.memory import Memory
from core.prompt_builder import build_prompt
from core.utils import extract_code
from core.docker_executor import run_python
from config.settings import CONTEXT_FILE


base_dir = os.path.dirname(os.path.dirname(__file__))

log_path = os.path.join(base_dir, "logs", "execution_logs.txt")

logging.basicConfig(
    filename=log_path,
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)


def load_context():

    context_path = os.path.join(base_dir, CONTEXT_FILE)

    try:
        with open(context_path, "r") as f:
            text = f.read()
            print("Loaded context:", len(text), "characters")
            return text
    except Exception as e:
        print("Context load error:", e)
        return ""


def main():

    context = load_context()

    llm = LocalLLM()

    memory = Memory()

    print("RLM REPL started")

    while True:

        user_input = input(">> ")

        logging.info(f"USER: {user_input}")

        prompt = build_prompt(user_input, memory.get(), context)

        response = llm.generate(prompt)

        print("\nLLM:\n", response)

        logging.info(f"LLM: {response}")

        code = extract_code(response)

        if code:

            print("\nExecuting inside docker...\n")

            logging.info("Running docker execution")

            result = run_python(code)

            print(result)

            logging.info(f"DOCKER RESULT: {result}")

        memory.add("user", user_input)
        memory.add("assistant", response)


if __name__ == "__main__":
    main()