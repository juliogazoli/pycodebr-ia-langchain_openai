# import os
# from decouple import config
# from langchain_openai import OpenAI
# from langchain_community.cache import InMemoryCache
# from langchain.globals import set_llm_cache

# os.environ['OPENAI_API_KEY'] = config('OPENAI_API_KEY')

# model = OpenAI()

# set_llm_cache(InMemoryCache())

# prompt = 'Me diga quem foi Alan Turing.'

# response1 = model.invoke(prompt)
# print(f'Chamada 1: {response1}')

# response2 = model.invoke(prompt)
# print(f'Chamada 2: {response2}')


import os
from decouple import config
from langchain_openai import OpenAI
from langchain_community.cache import SQLiteCache
from langchain.globals import set_llm_cache

os.environ['OPENAI_API_KEY'] = config('OPENAI_API_KEY')

model = OpenAI()

set_llm_cache(SQLiteCache(database_path='openai_cache.db'))

prompt = 'Me diga quem foi Albert Einstein.'

response1 = model.invoke(prompt)
print(f'Chamada 1: {response1}')

response2 = model.invoke(prompt)
print(f'Chamada 2: {response2}')
