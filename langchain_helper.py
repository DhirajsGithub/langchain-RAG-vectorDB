from secrets_file import GEMINI_KEY
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=GEMINI_KEY,
    temperature=0.6,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

# sequential chain can have multiple inputs multiple outputs
from langchain.chains import SequentialChain, LLMChain



def generate_restaurant_name_and_items(cuisine):
    prompt_template_name = PromptTemplate(
    input_variables=['cuisine'],
    template="""I want to open a restaurant for {cuisine} food. Suggest ONE fancy name for this only."""
    )
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="resturant_name")

    prompt_template_items = PromptTemplate(
        input_variables=['resturant_name'],
        template="""Suggest some menu items for {resturant_name} comma seperated inlude only menu item names"""
    )

    food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="menu_items")

    chain = SequentialChain(
        chains = [name_chain, food_items_chain],
        input_variables = ['cuisine'],
        output_variables = ['resturant_name', 'menu_items']
    )
    return chain({'cuisine': cuisine})


if __name__ == '__main__':
    print(generate_restaurant_name_and_items("Chinese"))