def perkalian(a):
    def dengan(b):
        return a*b
    return dengan

# Higher-Order Function (HOF)
def multiply_by_five(func):
    return func(5)

# Call perkalian with a value of 2
result_hof = multiply_by_five(perkalian(2))
print(result_hof)  # Output: 10

# Currying
result_currying = perkalian(2)(5)
print(result_currying)  # Output: 10
