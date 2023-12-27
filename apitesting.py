import os
from dotenv import load_dotenv
from langchain.chat_models import ChatAnthropic
from langchain.prompts import ChatPromptTemplate

load_dotenv(dotenv_path='.env')
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
ANTHROPIC_API_KEY= os.environ['ANTHROPIC_API_KEY']


# model = ChatAnthropic()


# prompt = ChatPromptTemplate.from_messages([
#     ("system", "You are a helpful chatbot"),
#     ("human", "Tell me a joke about {topic}"),
# ])

# chain = prompt | model
# res = chain.invoke({"topic": "capitalism"})

# print(res)


from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

template = """Question: {question}

Answer: Let's think step by step."""

prompt = PromptTemplate(template=template, input_variables=["question"])
llm = OpenAI()
llm_chain = LLMChain(prompt=prompt, llm=llm)
question = "What NFL team won the Super Bowl in the year Justin Beiber was born?"

res = llm_chain.run(question)
print(res)