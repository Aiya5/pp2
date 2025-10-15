import re

#Match a string that has an 'a' followed by zero or more 'b's------------------------------------------------------------------------
text = "ab abb abbb a b aaab"
pattern = r"ab*"
matches = re.findall(pattern, text)
print(matches)

#Match a string that has an 'a' followed by two to three 'b's-----------------------------------------------------------
text = "abb abbb abbbb ab a"
pattern = r"ab{2,3}"
matches = re.findall(pattern, text)
print(matches)

#Find sequences of lowercase letters joined with an underscore-----------------------------------------------------------
text = "Find_sequences of lowercase_letters joined_with an_underscore"
pattern = r"[a-z]+_[a-z]+"
matches = re.findall(pattern, text)
print(matches)

#Find sequences of one uppercase letter followed by lowercase letters--------------------------------------------------
text = "Find Sequences of one Uppercase letter Followed by lowercase Letters"
pattern = r"[A-Z][a-z]+"
matches = re.findall(pattern, text)
print(matches)

#Match a string that has an 'a' followed by anything, ending in 'b'--------------------------------------------------------
text = "acb a123b a-8_b ab axyzb"
pattern = r"a.*b"
matches = re.findall(pattern, text)
print(matches)

#Replace all occurrences of space, comma, or dot with a colon----------------------------------------------------
text = "Hello, world. This is a test"
pattern = r"[ ,.]"
result = re.sub(pattern, ":", text)
print(result)

#Convert snake case string to camel case-------------------------------------------------------------------------------
text = "convert_snake_case_string_to_camel_case"
def snake_to_camel(s):
    parts = s.split('_')
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])
print(snake_to_camel(text))

#Split a string at uppercase letters---------------------------------------------------------------------------
text = "SplitAStringAtUppercaseLetters"
parts = re.findall(r'[A-Z][^A-Z]*', text)
print(parts)

#Insert spaces between words starting with capital letters-----------------------------------------------------------
text = "InsertSpacesBetweenWordsStartingWithCapitalLetters"
result = re.sub(r"([a-z])([A-Z])", r"\1 \2", text)
print(result)

#Convert a given camel case string to snake case--------------------------------------------------------------------
text = "ConvertThisCamelCaseToSnakeCase"
result = re.sub(r'(?<!^)(?=[A-Z])', '_', text).lower()
print(result)