import inspect

def strict(func):
    sig = inspect.signature(func)
    params = sig.parameters
    
    def wrapper(*args):
        for i, arg in enumerate(args):
            param_name = list(params)[i]
            param_type = params[param_name].annotation
            if type(arg) is not param_type:
                raise TypeError(f"Argument {param_name} expected type {param_type}, got {type(arg).__name__}")
        return func(*args)
    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


try:
    print(sum_two(1, 2))
except TypeError as e:
    print(e)

try:
    print(sum_two(1, 2.4))
except TypeError as e:
    print(e)

try:
    print(sum_two(2, True))
except TypeError as e:
    print(e)

try:
    print(sum_two("123", 0))
except TypeError as e:
    print(e)

try:
    print(sum_two(True, False))
except TypeError as e:
    print(e)
