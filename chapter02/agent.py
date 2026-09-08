from chapter02.llm import LLM
from chapter02.step import Step
from chapter02.trajectory import Trajectory

class TinyAgent:
    """A minimal, modular e educational agent framework."""
    def __init__(self, llm: LLM):
        self.llm =llm
        self.trajectory = Trajectory()



