from chapter02.llm import LLM
from chapter02.agent import Step
from chapter02.trajectory import Trajectory

llm = LLM(model="gemma4:e4b")

response = llm.generate(
    [{"role": "user", "content": "Hi! How's life?"}]
)

print(response)

step = Step(answer=response.content)

print("\nStep:")
print(step)

trajectory = Trajectory()

trajectory.initialize("Quanto é 2 + 2?")

print("\nTrajectory:")
print(trajectory.runs)

trajectory.add(response)

print("\nTrajectory after adding the Step:")
print(trajectory.runs)