# import os
# from decouple import config
# from langchain_openai import OpenAI


# os.environ['OPENAI_API_KEY'] = config('OPENAI_API_KEY')

# model = OpenAI()

# response = model.invoke(
#     input='Quem foi Alan Turing?',
#     temperature=1,
#     max_tokens=500,
# )

# print(response)


import os
from decouple import config
from langchain_openai import ChatOpenAI


os.environ['OPENAI_API_KEY'] = config('OPENAI_API_KEY')



model = ChatOpenAI(
    model='gpt-3.5-turbo',
)

messages = [
    {'role': 'system', 'content': 'Você é um assistente que fornece informações sobre figuras históricas.'},
    {'role': 'user', 'content': 'Quem foi Alan Turing?'}
]

response = model.invoke(messages)

print(response)
print(response.content)
