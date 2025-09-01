from decouple import config
from agents import AsyncOpenAI,OpenAIChatCompletionsModel,Agent,Runner,set_tracing_disabled,RunContextWrapper,GuardrailFunctionOutput,OutputGuardrailTripwireTriggered,input_guardrail,InputGuardrailTripwireTriggered,output_guardrail,TResponseInputItem
from agents.extensions.handoff_prompt import RECOMMENDED_PROMPT_PREFIX
from data.hotel_data import res_info
from pydantic import BaseModel

set_tracing_disabled(True)

key = config('GEMINI_API_KEY')
base_url = config('gemini_base_url')



class MyDataOutput(BaseModel):
    is_hotel_query: bool
    is_hotel_account_or_tax_query:bool
    reason:str

client = AsyncOpenAI(api_key=key,base_url=base_url)
MODEL = OpenAIChatCompletionsModel(model="gemini-2.5-flash",openai_client=client)


# input guardrail
@input_guardrail
async def guardrail_input_function(ctx:RunContextWrapper[None],agent:Agent,input: str | list[TResponseInputItem]) -> GuardrailFunctionOutput:
    
    res = await Runner.run(
        guardrail_agent,
        input=input,
        context=ctx.context
    )
    return GuardrailFunctionOutput(
        output_info=res.final_output,
        tripwire_triggered=not res.final_output.is_hotel_query
    )
    
    
@output_guardrail
async def guardrail_output_function(ctx:RunContextWrapper[None],agent:Agent,input:str | list[TResponseInputItem] ):
    
    res = await Runner.run(
        guardrail_agent,
        input=input,
        context=ctx.context
    )
    return GuardrailFunctionOutput(
        output_info=res.final_output,
        tripwire_triggered=res.final_output.is_hotel_account_or_tax_query
    )    

    
guardrail_agent = Agent( 
    name = "Guardrail Agent",
    instructions='Check hotel related queries.and account or tax related query',
    model=MODEL,
    output_type=MyDataOutput
   
)

hotel_assistant = Agent(
    name="Hotel Customer Care Assistant",
    instructions=f"""{RECOMMENDED_PROMPT_PREFIX}
   Always use the res_info tool to answer questions about rooms, availability, or private rooms.
   If the tool gives structured data, extract the relevant information and explain it naturally.""",
    handoff_description="Helpful Hotel Assistant",
    model=MODEL,
    tools=[res_info],
    input_guardrails=[guardrail_input_function],
    output_guardrails=[guardrail_output_function]
   
   
)


while True:
    prompt = input("Enter your prompt: ")
    
    if prompt == "exit":
        break
    try:
    
        res=Runner.run_sync(
        starting_agent=hotel_assistant,
        input=prompt,
    ) 
        print(res.final_output)
    except InputGuardrailTripwireTriggered as e:
        print ("Please ask hotel related questions")   
        
    except OutputGuardrailTripwireTriggered as e:
        print("I am not able to provide personal info")    
    



