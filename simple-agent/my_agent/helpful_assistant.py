from agents import Agent
from my_config.gemini_config import GEMINI_MODEL
from my_config.groq_config import GROQ_MODEL



gemini_agent = Agent(name="Gemini Agent",
              instructions="You are a helpful assistant.",
              model=GEMINI_MODEL)

groq_agent = Agent(name="Groq Agent",
              instructions="You are my friend.",
              model=GROQ_MODEL)