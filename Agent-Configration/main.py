from agents import  Runner
from my_agents.agents import gemini_agent,groq_agent



res = Runner.run_sync(
    starting_agent=groq_agent,
    input="2+2",
)

print(res.final_output)