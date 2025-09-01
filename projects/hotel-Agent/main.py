from decouple import config
from agents import AsyncOpenAI,OpenAIChatCompletionsModel,Agent,Runner,function_tool,set_tracing_export_api_key,trace
from agents.extensions.handoff_prompt import RECOMMENDED_PROMPT_PREFIX
from data.hotel_data import res_info





openai_key = config("OPEN_API_KEY")
key = config('GEMINI_API_KEY')
base_url = config('gemini_base_url')

set_tracing_export_api_key(openai_key)

client = AsyncOpenAI(api_key=key,base_url=base_url)
MODEL = OpenAIChatCompletionsModel(model="gemini-2.5-flash",openai_client=client)

hotel_assistant = Agent(
    name="Hotel Customer Care Assistant",
    instructions=f"""{RECOMMENDED_PROMPT_PREFIX}
   Always use the res_info tool to answer questions about rooms, availability, or private rooms.
   If the tool gives structured data, extract the relevant information and explain it naturally.""",
    handoff_description="Helpful Hotel Assistant",
    model=MODEL,
    tools=[res_info]
   
)

agent = Agent(
    name="assistant",
    instructions='You are a helpful assistant that can hand off hotel questions to the hotel agent',
    model=MODEL,
    handoffs=[hotel_assistant]
   
)

while True:
    prompt = input("Enter your prompt: ")
    
    if prompt == "exit":
        break
    
    res=Runner.run_sync(
    starting_agent=agent,
    input=prompt,
) 
    print(res.final_output)
    



