def upper_case_string(input):
    if (input == ""):
        return ""
    
    first_char = input[0]
    rest_of_string = input[1:]
    
    first_capital = first_char.upper()
    leap_of_faith_result = upper_case_string(rest_of_string)

    return first_capital + leap_of_faith_result

upper_case_version = upper_case_string("hello")
print(upper_case_version)