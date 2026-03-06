from llama_cpp import Llama
from config.settings import MODEL_PATH

class LocalLLM:

    def __init__(self):
        self.llm = Llama(
            model_path=MODEL_PATH,
            n_ctx=4096,
            n_threads=12
        )

    def generate(self, prompt):

        output = self.llm(
            prompt,
            max_tokens=512,
            stop=["User:", "Assistant:"]
        )

        return output["choices"][0]["text"].strip()