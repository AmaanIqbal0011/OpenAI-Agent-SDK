from agents import RunContextWrapper


def dynamic_instruction(ctx:RunContextWrapper,agent):
    return f"user name is {ctx.context['name']} and city is {ctx.context['city']} and you are the helpful assistant that know about the user and answer my every questions"