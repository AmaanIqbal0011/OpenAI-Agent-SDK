from agents import RunContextWrapper
from pydantic import BaseModel


async def tool_validate(ctx:RunContextWrapper, agent):
    if ctx.context["age"] >= 18:
        return True
    return False