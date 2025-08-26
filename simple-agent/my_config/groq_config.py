from decouple import config
from agents import AsyncOpenAI, OpenAIChatCompletionsModel,Agent,Runner

key = config('GROQ_API_KEY')
base_url = config('base_url_groq')

client = AsyncOpenAI(api_key=key, base_url=base_url) 

GROQ_MODEL = OpenAIChatCompletionsModel(model="llama-3.3-70b-versatile",openai_client=client)

      