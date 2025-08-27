from decouple import config
from agents import AsyncOpenAI, OpenAIChatCompletionsModel,Agent,Runner,set_tracing_disabled
from output_type.schema import Data
set_tracing_disabled(True)




key = config('GEMINI_API_KEY')
base_url = config('base_url')   

client = AsyncOpenAI(api_key=key, base_url=base_url)

GEMINI_MODEL = OpenAIChatCompletionsModel(model="gemini-2.5-flash",openai_client=client)

gemini_agent = Agent(name="Gemini Agent",
              instructions="You are a helpful assistant.",
              model=GEMINI_MODEL,
              output_type=Data
              )



res = Runner.run_sync(starting_agent=gemini_agent, input="2+2=")

print(res.final_output)