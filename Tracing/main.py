from decouple import config
from agents import AsyncOpenAI,OpenAIChatCompletionsModel,Agent,Runner,function_tool,set_tracing_export_api_key
from agents.extensions.handoff_prompt import RECOMMENDED_PROMPT_PREFIX



@function_tool
def plus(a: int, b: int) -> str:
    """Returns the sum of two integers."""
    print("Adding numbers")
    return str(f'my answer is {a + b}')

openai_key = config("OPEN_API_KEY")
key = config('GEMINI_API_KEY')
base_url = config('gemini_base_url')

set_tracing_export_api_key(openai_key)

client = AsyncOpenAI(api_key=key,base_url=base_url)
MODEL = OpenAIChatCompletionsModel(model="gemini-2.5-flash",openai_client=client)

math_agent = Agent(
    name="math_assistant",
    instructions=f"""{RECOMMENDED_PROMPT_PREFIX}
    You are a helpful assistant that answer math questions""",
    handoff_description="you are the math assistant",
    model=MODEL,
    tools=[plus]
   
)

agent = Agent(
    name="assistant",
    instructions=f"""{RECOMMENDED_PROMPT_PREFIX}
    You are a helpful assistant that answer math questions""",
    model=MODEL,
    handoffs=[math_agent]
   
)

res=Runner.run_sync(
    starting_agent=agent,
    input="12+2"
) 


print(res.final_output)