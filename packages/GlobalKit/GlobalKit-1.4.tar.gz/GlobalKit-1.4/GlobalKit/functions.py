# Converts string into a list
def convert_to_list(string: str) -> list[str]:
    return [item for item in string]


# Checks if string is in any of alphabets
def check(string: str, *alphabets) -> bool:
    for alphabet in alphabets:
        if string in alphabet:
            return True

    return False


# Checks if string contains any spaces
def is_contains_spaces(string: str) -> bool:
    return any(char.isspace() for char in string)


# Checks if string contains any alphabetic characters
def is_contains_alphabetic(string: str) -> bool:
    return any(char.isalpha() for char in string)


# Checks if string contains any numbers
def is_contains_numbers(string: str) -> bool:
    return any(char.isdigit() for char in string)


# Checks if string contains any lowercase letters
def is_contains_lowercase(string: str) -> bool:
    return any(char.islower() for char in string)


# Checks if string contains any uppercase letters
def is_contains_uppercase(string: str) -> bool:
    return any(char.isupper() for char in string)


# Checks if string contains any special characters
def is_contains_special(string: str) -> bool:
    return any(not char.isalnum() for char in string)


# Checks if string contains any substring you want
def is_contains_substring(string: str, substring: str) -> bool:
    return substring in string
