import re

def dance(template_string: str, local_dict: dict, hyperparameters: dict = None) -> str:
    # Regular expression to find function calls or variables in {{}}
    pattern = r"\{\{(.*?)\}\}"

    # Find all matches in the template string
    matches = re.findall(pattern, template_string)

    for match in matches:
        # Check if it's a function call
        if '(' in match and ')' in match:
            function_name, parameters = match.split('(')
            parameters = parameters.rstrip(')')

            # Execute the function with the parameters and get the result
            try:
                result = eval(f"{function_name}({parameters})", globals(), local_dict)
            except Exception as e:
                return f"The function failed to bring the data: {str(e)}"

        else:
            # It's a variable
            variable_name = match

            # Get the value of the variable
            try:
                if hyperparameters and variable_name in hyperparameters:
                    result = hyperparameters[variable_name]
                else:
                    result = eval(variable_name, globals(), local_dict)
            except Exception as e:
                return f"The variable failed to bring the data: {str(e)}"

        # Replace the function call or variable in the template string with the result
        template_string = template_string.replace(f"{{{{{match}}}}}", str(result))

    return template_string


def name() -> str:
    return f"Marcelo"

if __name__ == "__main__":
    print(dance("My name is {{name()}}, from {{country}}!", locals(), {'country': 'Chile'}))
