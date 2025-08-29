from decouple import config
from agents import AsyncOpenAI,OpenAIChatCompletionsModel,Agent,Runner,function_tool,FunctionTool,RunContextWrapper,set_tracing_disabled,RunConfig
from pydantic import BaseModel
from validator.valid_tool import tool_validate

set_tracing_disabled(True)

key = config('GEMINI_API_KEY')
base_url = config('gemini_base_url')

@function_tool
def plus(a: int, b: int) -> str:
    """This is plus function that adds two numbers."""
    print("Plus function called")
    return f"The sum of {a} and {b} is {a + b} and my answer is {a + b}"

class MyToolSchema(BaseModel):
    n1: int
    n2: int
    
async def subtract_function(ctx:RunContextWrapper, args):
    obj = MyToolSchema.model_validate_json(args)
    return f"The subtraction of {obj.n1} and {obj.n2} is {obj.n1 - obj.n2} and my answer is {obj.n1 - obj.n2}"    

subtract = FunctionTool(
     name="subtract",
     description="subtract function",
     params_json_schema=MyToolSchema.model_json_schema(),
     on_invoke_tool=subtract_function,
     is_enabled=tool_validate
)



client = AsyncOpenAI(api_key=key, base_url=base_url)

model = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=client
)

Assistant = Agent(
    name="Assistant",
    instructions="You are a helpful assistant",
    model=model,
    tools=[plus,subtract]
    )

res = Runner.run_sync(
    starting_agent=Assistant, 
    input="2-2=",
    context={"age": 8}
    )

print(res.final_output)
