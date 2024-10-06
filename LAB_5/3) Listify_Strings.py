def listify_strings(strings):
    return list(map(list, strings))


strings = ["hello", "world", "python"]
listified_strings = listify_strings(strings)
print(listified_strings)  