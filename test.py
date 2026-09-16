from chapter02.llm import LLM
from chapter02.agent import TinyAgent
from chapter02.trajectory import Trajectory

llm = LLM(model="gemma4:e4b")

trajectory = Trajectory()

trajectory.initialize("Quanto é 2 + 2?")

print("Trajectory before adding a Step:")
print(trajectory.runs)


agent = TinyAgent(llm)

answer = agent.run("Quanto é 2 + 2?")

print("\nAgent answer:")
print(answer)

print("\nAgent trajectory:")
print(agent.trajectory.runs)