import yaml
from helpers import execute_function_from_string, get_function_name
from openai_code import explain_code, generate_inputs, generate_unittest_advanced

def unittest_from_file(file_path:str, openai_api_key:str) -> None:
    """Generates unittests for each function in the file, given a file_path and an api_key. Functions are assumed to have their definition starting with def."""
    with open(file_path, "r") as file:
        python_code = file.read()
    code_split = python_code.split("\ndef")
    python_fcts = [code_split[0] + "\ndef" + code_piece for code_piece in code_split[1:]]
    for fct in python_fcts:
        code_explanation = explain_code(fct, openai_api_key)
        input_list = generate_inputs(fct, code_explanation, openai_api_key)
        output_list = [0]*len(eval(input_list))
        for i, input in enumerate(eval(input_list)):
            try:
                output_list[i] = execute_function_from_string(fct, *input)
            except TypeError:
                output_list[i] = execute_function_from_string(fct, input)
        unittest = generate_unittest_advanced(fct, code_explanation, input_list, output_list, openai_api_key)
        function_name = get_function_name(fct)
        save_name = f"tests/test_{function_name}.py"
        complete_unittest = code_split[0] + f"\nfrom ..{file_path.split(".")[0]} import {function_name}\n" + unittest
        with open(save_name, "w") as file:
            file.write(complete_unittest)
        print(f"Python code has been written to '{save_name}'")

if __name__ == "__main__":
    file_path = 'my_code.py'
    with open('config.yml', 'r') as file:
        config = yaml.safe_load(file)
    openai_api_key = config["openai_key"]
    unittest_from_file(file_path, openai_api_key)