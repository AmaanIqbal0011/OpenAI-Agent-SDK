from decouple import config
from agents import AsyncOpenAI,OpenAIChatCompletionsModel,Agent,Runner,set_tracing_disabled,handoff,RunContextWrapper,function_tool
from agents.extensions.handoff_prompt import RECOMMENDED_PROMPT_PREFIX
from agents.extensions import handoff_filters
from pydantic import BaseModel

set_tracing_disabled(True)

async def res(ctx:RunContextWrapper,agent_base =None):
    if ctx.context["age"] >= 18:
        return True
    return False


key = config('GEMINI_API_KEY')
base_url = config("gemini_base_url")

client = AsyncOpenAI(api_key=key,base_url=base_url)
MODEL = OpenAIChatCompletionsModel(model="gemini-2.5-flash",openai_client=client)

@function_tool
def weather(city: str) -> str:
    """Get the current weather in a given city."""
    print("weather function called...")
    return f"The weather in {city} is sunny."


math_agent = Agent(
    name="Math Agent",
    instructions=f"""{RECOMMENDED_PROMPT_PREFIX}
    You are a helpful assistant that answer math questions""",
    model=MODEL,
    handoff_description="this is a math agent, if the question is not math related, please handoff to the english agent"
   
)

class InputData(BaseModel):
    """Input data for the service function."""
  
    result:str
    

async def service(ctx:RunContextWrapper,input_data:InputData):
   print(ctx.context)
   print("service function called...")

   print(f"result is ",input_data.result)


math_teacher = handoff(
    agent=math_agent,
    tool_name_override="Math_Teacher",
    tool_description_override="Math Teacher",
    on_handoff=service,
    input_type=InputData,
    input_filter=handoff_filters.remove_all_tools,
    is_enabled=res
)


agent = Agent(
    name="Gemini Agent",
    instructions="You are a helpful assistant,that can answer any question using the tools and handoff to math teacher if the question is math related and also use weather tool to get the weather of any city and if the question is not math related or weather related, answer it yourself using your own knowledge and do not handoff to math teacher and do not use weather tool",
    model=MODEL ,
    handoffs=[math_teacher],
    tools=[weather]
   
)

res=Runner.run_sync(
    starting_agent=agent,
    input="karachi ka weather kay sa hai,and 12+14=?",
    context={"role":"user","age":10}
) 


print(res.final_output)

