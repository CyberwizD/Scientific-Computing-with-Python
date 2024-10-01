# List Comprehension

# List Comprehension is a way to construct a new Python list from an iterable type
# In this project, building a program that takes a camelCase or PascalCase formatted string as input
# and converts that to a snake_case formatted string using two approaches.
# First, using a for loop and then list comprehension to achieve the same results.

# Using for loop to build a case converter program

def convert_to_snake_case(pascal_or_camel_cased_string):
    snake_cased_char_list = []
    for char in pascal_or_camel_cased_string:
        if char.isupper():
            converted_character = '_' + char.lower()
            snake_cased_char_list.append(converted_character)
        else:
            snake_cased_char_list.append(char)
    snake_cased_string = ''.join(snake_cased_char_list)
    clean_snake_cased_string = snake_cased_string.strip('_')

    return clean_snake_cased_string

def main():
    print(convert_to_snake_case('aLongAndComplexString'))

main()

# Using a list comprehension to build a case converter program
# In Python, a list comprehension is a construct that allows you to generate a new list
# by applying an expression to each item in an existing iterable and optionally filtering items with a condition.

def convert_to_snake_case(pascal_or_camel_cased_string):
    snake_cased_char_list = [
        '_' + char.lower() if char.isupper()
        else char
        for char in pascal_or_camel_cased_string
    ]

    return ''.join(snake_cased_char_list).strip('_')

def main():
    print(convert_to_snake_case('aLongAndComplexString'))

if __name__ == '__main__':
    main()
