from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.schema import StrOutputParser

def code_generation(code, openai_api_key):
    prompt = PromptTemplate.from_template(
        """**Role**: You are a software programmer.
        **Task**: As a programmer, you are required to complete the function. Use a Chain-of-Thought approach to break
        down the problem, create pseudocode, and then write the code in Python language. Ensure that your code is
        efficient, readable, and well-commented.
        For example:
        **Input Code Snippet**:
        ```python
        {code}
        # TODO: Implement the necessary logic
        pass
        # Add your code here to complete the function
        ```
        **Instructions**:
        1. **Understand and Clarify**: Make sure you understand the task.
        2. **Algorithm/Method Selection**: Decide on the most efficient way.
        3. **Pseudocode Creation**: Write down the steps you will follow in pseudocode.
        4. **Code Generation**: Translate your pseudocode into executable Python code.  """  
    )
    runnable = (
    prompt
    | ChatOpenAI(model_name="gpt-4", openai_api_key=openai_api_key, temperature=0)
    | StrOutputParser()
    )
    return runnable.invoke({"code": code})

def test_generation(code, openai_api_key):
    prompt = PromptTemplate.from_template(
        """**Role**: As a tester, your task is to create comprehensive test cases for the incomplete `has_close_elements`
        function. These test cases should encompass Basic, Edge, and Large Scale scenarios to ensure the code's
        robustness, reliability, and scalability.
        **Input Code Snippet**:
        ```python
        {code}
        ```
        **1. Basic Test Cases**:
        - **Objective**: To verify the fundamental functionality of the `has_close_elements` function under normal
        conditions.
        **2. Edge Test Cases**:
        - **Objective**: To evaluate the function's behavior under extreme or unusual conditions.
        **3. Large Scale Test Cases**:
        - **Objective**: To assess the function’s performance and scalability with large data samples.
        **Instructions**:
        - Implement a comprehensive set of test cases following the guidelines above.
        - Ensure each test case is well-documented with comments explaining the scenario it covers.
        - Pay special attention to edge cases as they often reveal hidden bugs.
        - For large-scale tests, focus on the function's efficiency and performance under heavy loads."""
    )
    runnable = (
    prompt
    | ChatOpenAI(model_name="gpt-4", openai_api_key=openai_api_key, temperature=0)
    | StrOutputParser()
    )
    return runnable.invoke({"code": code})