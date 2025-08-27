from decouple import config
from agents import  AsyncOpenAI,OpenAIChatCompletionsModel,set_tracing_disabled

key = config('GEMINI_API_KEY')
base_url = config('base_url')
set_tracing_disabled(True)

client = AsyncOpenAI(api_key=key,base_url=base_url)

gemini_model = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=client
    
)