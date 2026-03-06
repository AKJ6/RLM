def build_prompt(user_input, memory, context):

    system = "You are a helpful assistant."

    prompt = "<s>[INST] <<SYS>>\n"
    prompt += system + "\n"
    prompt += "<</SYS>>\n\n"

    for role, msg in memory:
        if role == "user":
            prompt += msg + " [/INST] "
        else:
            prompt += msg + " </s><s>[INST] "

    prompt += user_input + " [/INST]"

    return prompt