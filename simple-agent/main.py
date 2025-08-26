from agents import Runner,set_tracing_disabled
from my_agent.helpful_assistant import gemini_agent,groq_agent



set_tracing_disabled(True)

res = Runner.run_sync(starting_agent=groq_agent, input="2+2=")

print(res.final_output)