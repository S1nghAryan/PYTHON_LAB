def triple_numbers(numbers):
    return list(map(lambda x: x * 3, numbers))

numbers = [1, 2, 3, 4, 5]
tripled_numbers = triple_numbers(numbers)
print(tripled_numbers) 