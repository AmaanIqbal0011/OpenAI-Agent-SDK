from decouple import config
from agents import AsyncOpenAI,OpenAIChatCompletionsModel,Agent,Runner,set_tracing_disabled,function_tool,RunContextWrapper
from instruction.dynamic_instruction import dynamic_instruction

set_tracing_disabled(True)

key = config('GEMINI_API_KEY')
base_url = config('gemini_base_url')

client = AsyncOpenAI(api_key=key,base_url=base_url)

MODEL = OpenAIChatCompletionsModel(model="gemini-2.5-flash",openai_client=client)

@function_tool
def get_age(ctx:RunContextWrapper) -> str:
    """age function"""
    print("age tool called")
    return f'your age is {ctx.context["age"]}'

agent = Agent(
    name="Gemini Agent",
    instructions=dynamic_instruction,
    model=MODEL,
    tools=[get_age]
)

res=Runner.run_sync(
    starting_agent=agent,
    input="Hello,What is my name and what is my age?",
    context={"name":"Aman","age":25,"city":"New York"}
) 


print(res.final_output)