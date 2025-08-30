from decouple import config
from agents import AsyncOpenAI,OpenAIChatCompletionsModel,Agent,RunConfig,Runner,set_tracing_disabled,function_tool,RunContextWrapper
from dataclasses import dataclass

set_tracing_disabled(True)

key = config('GEMINI_API_KEY')
base_url = config('gemini_base_url')




def dynamic_instruction(ctx:RunContextWrapper,agent):
    return f"user name is{ctx.context["name"]}  and age is {ctx.context["age"]} and you are the helpful assistant that answer every question of the user"


@function_tool
def userInfo(ctx:RunContextWrapper) -> str:
    """User-info function"""
    print("userInfo function called")
    return f"The user {ctx.context["name"]} is {ctx.context["age"]} years old"


client = AsyncOpenAI(api_key=key, base_url=base_url)

gemini_model = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=client
    )

agent = Agent(
    name="Gemini Agent",
    instructions=dynamic_instruction,
    model=gemini_model,
    tools=[userInfo]
)


while True:
    prompt = input("Enter your prompt:  ")
    if prompt.lower() == "exit":
        break
    
    res = Runner.run_sync(
        starting_agent=agent, 
        input=prompt,
        context={"name":"Amaan","age":30},
    )
    print(res.final_output)