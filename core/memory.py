from collections import deque
from config.settings import MEMORY_SIZE

class Memory:

    def __init__(self):
        self.messages = deque(maxlen=MEMORY_SIZE)

    def add(self, role, message):
        self.messages.append((role, message))

    def get(self):
        return list(self.messages)