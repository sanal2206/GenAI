import os
os.environ['GOOGLE_API_KEY']='AIzaSyDZGb5uGmsVEPsJiDF3bUFWcysWFv1Ud44'

from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="models/gemini-2.5-flash-lite",
    temperature=0.7
)

from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper


wiki=WikipediaQueryRun(
    api_wrapper=WikipediaAPIWrapper(top_k_results=1)

)

tools=[wiki]

llm_with_tools=llm.bind_tools(tools)

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

prompt=ChatPromptTemplate.from_messages([
    ("system","You are a factual research assistant. The current year is 2026"),
    ("human","{question}")
])

chain=prompt | llm_with_tools | StrOutputParser()

response = chain.invoke({
    "question": "Elon Musk was born on June 28, 1971. Assuming the current year is 2026, what is his age?"
})

print(response)
