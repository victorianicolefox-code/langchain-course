from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
#from langchain_ollama import ChatOllama

load_dotenv()

def main():
    print("Hello from langchain-course!")
    information = """
    Harry Potter is a wizard who lives in the Harry Potter book series. He is a student at Hogwarts School of Witchcraft and Wizardry. Voldermort killed his parents.
    """

    summary_template = f"""
        given the following information {information} about a person, please create a short summary and two interesting facts about them:
        1. a short summary of the person
        2. two interesting facts about them        
        """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template,
    )

    # llm = ChatOllama(temperature=0, model="gemma3:270m")
    llm = ChatOpenAI(temperature=0, model="gpt-5")
    chain = summary_prompt_template | llm 
    response = chain.invoke({"information": information})
    print(response.content)

if __name__ == "__main__":
    main()
