from decouple import config
from agents import AsyncOpenAI,OpenAIChatCompletionsModel,Agent,Runner,set_tracing_disabled,function_tool
from agents.extensions.handoff_prompt import RECOMMENDED_PROMPT_PREFIX

set_tracing_disabled(True)

@function_tool
def plus(a: int, b: int) -> str:
    """Returns the sum of two integers."""
    print("Adding numbers")
    return str(f'my answer is {a + b}')

key = config('GEMINI_API_KEY')
base_url = config('gemini_base_url')

client = AsyncOpenAI(api_key=key,base_url=base_url)
MODEL = OpenAIChatCompletionsModel(model="gemini-2.5-flash",openai_client=client)


math_agent = Agent(
    name="Math Agent",
    instructions=f"""{RECOMMENDED_PROMPT_PREFIX}
    You are a helpful assistant that answer math questions""",
    model=MODEL,
    tools=[plus],
    handoff_description="this is a math agent, if the question is not math related, please handoff to the english agent"
   
)
english_agent = Agent(
    name="English Agent",
    instructions=f"""{RECOMMENDED_PROMPT_PREFIX}
    You are a helpful assistant that answer english questions and always say Hello.""",
    model=MODEL,
    handoff_description="this is an english agent, if the question is not english related, please handoff to the math agent"
   
)

agent = Agent(
    name="Gemini Agent",
    instructions="You are a helpful assistant",
    model=MODEL ,
    handoffs=[math_agent,english_agent]
   
)

res=Runner.run_sync(
    starting_agent=agent,
    input="Hello"
) 

print(res.last_agent.name)
print(res.final_output)