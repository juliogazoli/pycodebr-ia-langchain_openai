import os
from decouple import config
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate


os.environ['OPENAI_API_KEY'] = config('OPENAI_API_KEY')

model = ChatOpenAI(
    model='gpt-3.5-turbo',
)

template = '''
Traduza o texto do {idioma_1} para o {idioma_2}:
{texto}
'''

prompt_template = PromptTemplate(
    template=template
)

prompt = prompt_template.format(
    idioma_1='português',
    idioma_2='francês',
    texto='Boa tarde!',
)

response = model.invoke(prompt)

print(response.content)
