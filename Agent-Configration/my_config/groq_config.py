from decouple import config
from agents import AsyncOpenAI,OpenAIChatCompletionsModel,set_tracing_disabled

key = config('GROQ_API_KEY')
base_url = config('base_url_groq')

client = AsyncOpenAI(
    api_key=key,
    base_url=base_url
)

Groq_model = OpenAIChatCompletionsModel(
    model='llama-3.3-70b-versatile',
    openai_client=client 
)