

from dotenv import load_dotenv
import os
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

os.environ['GOOGLE_API_KEY']=GOOGLE_API_KEY

"""Google gemini flast 2.5 lite is using as LLM model"""
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = ChatGoogleGenerativeAI(
    model="models/gemini-2.5-flash-lite",
    temperature=0.7
)

def generate_resturant_name_and_items(cuisine):
    # Chain 1: Restaurant name
    prompt_template_name = PromptTemplate(
        input_variables=['cuisine'],
        template="i want to open a restaurant for {cuisine} food. Suggest a fancy name for this. Return only the name, nothing else."
    )

    name_chain = prompt_template_name | llm | StrOutputParser()
    restaurant_name = name_chain.invoke({"cuisine": cuisine})

    # Chain 2: Menu items
    prompt_template_items = PromptTemplate(
        input_variables=['restaurant_name'],
        template="suggest some menu items for {restaurant_name}. Return as a comma separated string"
    )

    food_items_chain = prompt_template_items | llm | StrOutputParser()
    menu_items = food_items_chain.invoke({"restaurant_name": restaurant_name})

    return {
        'restaurant_name': restaurant_name,
        'menu_items': menu_items
    }


if __name__ == "__main__":
    print(generate_resturant_name_and_items('italian'))