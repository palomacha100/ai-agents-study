from chapter02.llm import LLM

llm = LLM(model="gemma4:e4b")

response = llm.generate(
    [{"role": "user", "content": "Hi! How's life?"}]
)

print(response)