from agents import  AsyncOpenAI,OpenAIChatCompletionsModel,Agent,Runner,set_tracing_disabled,RunConfig
from my_config.gemini_config import gemini_model
from my_config.groq_config import Groq_model

gemini_agent = Agent(
    name="Gemini Agent",
    instructions="You are a helpful assistant.",
    model=gemini_model
    
)

groq_agent = Agent(
    name="Groq",
    instructions="you are my best friend",
    model=Groq_model
    
)

runner_level_config_agent = Agent(
    name="Runner",
    instructions="you are a islamic scholar.say always salam after the conversation"
)