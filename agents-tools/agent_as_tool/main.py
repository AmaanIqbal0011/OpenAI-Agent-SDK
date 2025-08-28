from decouple import config
from agents import AsyncOpenAI,OpenAIChatCompletionsModel,Agent,Runner,set_tracing_disabled

set_tracing_disabled(True)

key = config('GEMINI_API_KEY')
base_url = config('gemini_base_url')

client = AsyncOpenAI(api_key=key,base_url=base_url)

MODEL = OpenAIChatCompletionsModel(model="gemini-2.5-flash",openai_client=client)

math_agent = Agent(
    name="Math Agent",
    instructions="You are a helpful assistant that answer math questions and always say Hello,",
    model=MODEL
   
)

agent = Agent(
    name="Gemini Agent",
    instructions="You are a helpful assistant that answer my every questions",
    model=MODEL ,
    tools=[math_agent.as_tool(
        tool_name="Math_Agent",
        tool_description="Useful for when you need to answer questions about math"
    )]
)

res=Runner.run_sync(
    starting_agent=agent,
    input="2+2"
) 

print(agent.tools)
print(res.final_output)