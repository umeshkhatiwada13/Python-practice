# function for ceaser cypher conversion
def ceaser_cypher(input_string, shift_number):
    converted_text = ""
    for str in input_string:
        if str.isalpha():
            # convert the alphabet to number and add shift provided by user
            numeric_for_alphabet = ord(str) + shift_number
            # if the numerical value is greater than that of z,
            # subtract 26 for stating from a
            if numeric_for_alphabet > ord('z'):
                numeric_for_alphabet -= 26
            # convert the final number back to alphabet
            final_text = chr(numeric_for_alphabet)
            converted_text += final_text
    return converted_text


init_string = str(input("Enter the String for conversion : "))
shift_number = int(input("Enter the shift : "))
print(f"String before shift {init_string}")
print(f"String after {shift_number} shifts : {ceaser_cypher(init_string, shift_number)}")
