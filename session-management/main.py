import asyncio
from decouple import config
from agents import AsyncOpenAI,OpenAIChatCompletionsModel,Agent,Runner,SQLiteSession,set_tracing_disabled
from dataclasses import dataclass

set_tracing_disabled(True)

key = config('GEMINI_API_KEY')
base_url = config('gemini_base_url')
session = SQLiteSession("User_2","conversion.db")

# async def main():
#     await session.clear_session()
#     user_data = await session.get_items()
#     for user in user_data:
#         print(f"{user['role']}:{user['content']}")

    
# asyncio.run(main())    


client = AsyncOpenAI(api_key=key, base_url=base_url)

gemini_model = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=client
    )

agent = Agent(
    name="Gemini Agent",
    instructions="You are the personal assistant",
  
    model=gemini_model,
)


while True:
    prompt = input("Enter your prompt:  ")
    if prompt.lower() == "exit":
        break
    
    res = Runner.run_sync(
        starting_agent=agent, 
        input=prompt,
        session=session
    )
    print(res.final_output)