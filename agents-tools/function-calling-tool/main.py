from decouple import config
from agents import AsyncOpenAI,OpenAIChatCompletionsModel,Agent,RunConfig,Runner,set_tracing_disabled,ModelSettings
from agents.agent import StopAtTools
from agents import function_tool,enable_verbose_stdout_logging
from user_data import fetch_user_data,fetch_user_data_by_id
set_tracing_disabled(True)

key = config('GEMINI_API_KEY')
base_url = config('gemini_base_url')

@function_tool
def plus(a: int, b: int) -> str:
    """This is plus function that adds two numbers."""
    print("Plus function called")
    return f"The sum of {a} and {b} is {a + b} and my answer is {a + b}"

@function_tool
async def subtract(a: int, b: int) -> str:
    """This is plus function that subtract two numbers."""
    print("Subtract function called")
    return f"The sum of {a} and {b} is {a - b} and my answer is {a - b}"




client = AsyncOpenAI(api_key=key, base_url=base_url)

gemini_model = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=client
    )

agent = Agent(
    name="Gemini Agent",
    instructions="You are a helpful assistant that answer my every question using LLm or tools.",
    tools=[plus, subtract, fetch_user_data, fetch_user_data_by_id],
    tool_use_behavior=StopAtTools(stop_at_tool_names=["plus","subtract"]),
    model_settings=ModelSettings(tool_choice="subtract",parallel_tool_calls=False),
    reset_tool_choice=True
    )

res = Runner.run_sync(
    starting_agent=agent, 
    input="2+2-2+4+5-2",
    run_config = RunConfig(model=gemini_model,model_provider=client),
    max_turns=5
)

print(res.final_output)