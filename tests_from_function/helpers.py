def get_function_name(func_string:str) -> str:
    """Gets function name from a function string"""
    # Extract the function definition substring
    start_index = func_string.find("def ")
    end_index = func_string.find("(")
    if start_index == -1 or end_index == -1:
        raise ValueError("No function definition found in the provided string.")

    # Extract the function definition substring
    function_definition = func_string[start_index:end_index]
    function_name = function_definition.split("(")[0][4:]
    return function_name

def execute_function_from_string(func_string:str, *args, **kwargs):
    """Executes function from a function string and given arguments"""
    # Execute the function definition in the current scope
    exec(func_string)

    # Get the function from locals    
    function_name = get_function_name(func_string)
    function_to_call = locals().get(function_name)

    # Check if the function exists
    if function_to_call is not None:
        # Call the function with arguments and return the result
        return function_to_call(*args, **kwargs)
    else:
        raise ValueError("No function named 'function' found in the provided string.")