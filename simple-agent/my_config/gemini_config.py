from decouple import config
from agents import AsyncOpenAI, OpenAIChatCompletionsModel,Agent,Runner


key = config('GEMINI_API_KEY')
base_url = config('base_url')   

client = AsyncOpenAI(api_key=key, base_url=base_url)

GEMINI_MODEL = OpenAIChatCompletionsModel(model="gemini-2.5-flash",openai_client=client)