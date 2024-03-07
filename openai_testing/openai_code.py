from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.schema import StrOutputParser

def explain_code(code, openai_api_key):
    prompt = PromptTemplate.from_template(
            """
            You are an artificial intelligence language model which goal is to explain a code piece, given the full code.
            Code: {code}
            Let's think step by step.
            Answer:"""
    )
    runnable = (
    prompt
    | ChatOpenAI(openai_api_key=openai_api_key, temperature=0)
    | StrOutputParser()
    )
    return runnable.invoke({"code": code})

def generate_inputs(code, openai_api_key):
    prompt = PromptTemplate.from_template(
            """
            You are an artificial intelligence language model which goal is to generate example inputs to be used within a given code.

            Code: def multiply(a:float, b:float) -> float: return a*b
            Example Inputs: a=5.1, b=10.2

            Code: def create_df(address_list:list[str], num_list:list[int]) -> pd.DataFrame: return pd.DataFrame("address": address_list, "num": num_list)
            Example Inputs: address_list=["rue de la fontaine"], num_list=[10]

            Code: {code}
            Example Inputs:"""
    )
    runnable = (
    prompt
    | ChatOpenAI(openai_api_key=openai_api_key, temperature=0)
    | StrOutputParser()
    )
    return runnable.invoke({"code": code})

def generate_unittest(code, code_explanation, inputs, openai_api_key):
    prompt = PromptTemplate.from_template(
            """
            You are an artificial intelligence language model which goal is to generate a unittest code from a piece of code, using the mentioned inputs. You can help yourself from the code explanation.
            Code: {code}
            Code explanation: {code_explanation}
            Inputs: {inputs}
            Only return the test class. Do not return anything else.
            Unittest Code:"""
    )
    runnable = (
    prompt
    | ChatOpenAI(openai_api_key=openai_api_key, temperature=0)
    | StrOutputParser()
    )
    return runnable.invoke({"code": code, "code_explanation": code_explanation, "inputs": inputs})