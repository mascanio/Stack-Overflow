from types import FunctionType

def function_builder(builder_param: str) -> FunctionType:
    def inner_function(inner_function_param: int) -> int:
        print(f"I'm inner_function, called with {inner_function_param}")
        print(f"I'm built from function_builder, built with {builder_param}")

        return inner_function_param
    
    return inner_function

# Call function builder
# build a function
built_function = function_builder('Hello world!')
print(f'Type of built_function is {type(built_function)}')
# Type of built_function is <class 'function'>
print('')

# Call built_function as a normal function
result = built_function(42)
print(f'Result of calling built_function is {result}')
# I'm inner_function, called with 42
# I'm built from function_builder, built with Hello world!
# Result of calling built_function is 42

print('')

# Calling it again
result = built_function(27)
print(f'Result of calling built_function is {result}')
# I'm inner_function, called with 27
# I'm built from function_builder, built with Hello world!
# Result of calling built_function is 27