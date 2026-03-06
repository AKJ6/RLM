# RLM – Recursive Language Model with Docker Execution

This project runs a **local LLM agent** that can:

- chat with the user
- read a long context document
- remember recent messages
- generate Python code
- execute that code safely inside Docker

Everything runs **locally** using a GGUF model with `llama-cpp-python`.

---

# Project Structure


rlm/
│
├── models/
│ └── llama-2-7b-chat.gguf
│
├── context/
│ └── long_document.txt
│
├── docker/
│ ├── Dockerfile
│ └── run_container.sh
│
├── core/
│ ├── llm.py
│ ├── memory.py
│ ├── prompt_builder.py
│ ├── docker_executor.py
│ └── utils.py
│
├── repl/
│ └── repl.py
│
├── config/
│ └── settings.py
│
├── logs/
│ └── execution_logs.txt
│
├── requirements.txt
├── docker-compose.yml
└── README.md


---

# Setup

### 1. Create a Python environment


python -m venv my
source my/bin/activate


### 2. Install dependencies


pip install -r requirements.txt


---

# Download the Model

Download a GGUF model from HuggingFace.

Recommended:


hf download TheBloke/Llama-2-7B-Chat-GGUF
llama-2-7b-chat.Q4_K_M.gguf
--local-dir models


Ensure the model exists in:


models/


Update the path if needed in:


config/settings.py


---

# Docker Setup

Make sure Docker works.


docker run hello-world


If Docker requires sudo, enable user access:


sudo usermod -aG docker $USER
newgrp docker


---

# Run the System

Just run:


python repl/repl.py


