from agents import  Runner,RunConfig
from my_agents.agents import gemini_agent,groq_agent,runner_level_config_agent
from my_config.gemini_config import gemini_model,client


res = Runner.run_sync(
    starting_agent=runner_level_config_agent,
    input="2+2",
    run_config=RunConfig(
        model=gemini_model,
        model_provider=client
        
    )
)

print(res.final_output)