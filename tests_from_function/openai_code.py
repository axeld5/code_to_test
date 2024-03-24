from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.schema import StrOutputParser

def explain_code(code:str, openai_api_key:str) -> str:
    """Generation of a code explanation given code file and openai key"""
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

def generate_inputs(code:str, code_explanation:str, openai_api_key:str) -> str:
    """Generation of a list of inputs given code text, code explanation and openai key"""
    prompt = PromptTemplate.from_template(
            """
            You are an artificial intelligence language model which goal is to generate a list of at least 5 example inputs to be used within a given code.
            Through the exploitation of a code explanation, your goal is also to generate examples which are as diverse as possible, in order to tackle as many edge cases as can be done.
            Therefore: vary the amount of inputs if that is a parameter, the values of the inputs... In order for the tests to cover as wide as possible.

            Code: def multiply(a:float, b:float) -> float: return a*b
            Code explanation: This code multiplies two floats.
            Example Inputs: [(5.1, 10.2), (500.3, 4.0), (12.3, 4.29), (-10.0, 3), (31.2, 5.4)]

            Code: def create_df(address_list:list[str], num_list:list[int]) -> pd.DataFrame: return pd.DataFrame("address": address_list, "num": num_list)
            Code explanation: This code creates a dataframe from a list of adresses and numbers related to those addresses.
            Example Inputs: [(["rue de la fontaine"], [10]), ..., (["baker street", "sesame avenue"], [222, 300])]

            Code: {code}
            Code explanation: {code_explanation}
            Example Inputs:"""
    )
    runnable = (
    prompt
    | ChatOpenAI(openai_api_key=openai_api_key, temperature=0)
    | StrOutputParser()
    )
    return runnable.invoke({"code": code, "code_explanation": code_explanation})

def generate_unittest_advanced(code:str, code_explanation:str, inputs:str, outputs:str, openai_api_key:str) -> str:
    """Generation of unittests given code text, code explanation, inputs, outputs and openai key"""
    prompt = PromptTemplate.from_template(
        """
        You are an artificial intelligence language model which goal is to generate a unittest code from a piece of code, using the mentioned inputs and their related outputs. You can help yourself from the code explanation.
        Code: {code}
        Code explanation: {code_explanation}
        Input_list: {inputs}
        Output_list: {outputs}
        Only return the test class, without any imports or function definition.
        Unittest Code:"""
    )
    runnable = (
    prompt
    | ChatOpenAI(openai_api_key=openai_api_key, temperature=0)
    | StrOutputParser()
    )
    return runnable.invoke({"code": code, "code_explanation": code_explanation, "inputs": inputs, "outputs": outputs})