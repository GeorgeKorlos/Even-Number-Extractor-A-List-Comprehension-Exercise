list_of_strings = input().split(',')

list_of_numbers = [int(strings) for strings in list_of_strings]

result = [even for even in list_of_numbers if even % 2 == 0]

print(result)