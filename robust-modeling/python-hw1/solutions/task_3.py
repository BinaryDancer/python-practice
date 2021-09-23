def mutate_string(string: str, index: int, char: str) -> str:
    return string[:index] + char + string[index+1:]


assert mutate_string("abracadabra", 5, "X") == "abracXdabra"  # should be true