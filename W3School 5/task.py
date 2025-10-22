import re
'''text = "ab abb abbb a b aaab"
matches = re.findall("ab*", text)
print(matches)
'''
'''
txt = "The rain in Spain 9"
pattern=r"\d"
x = re.search(pattern, txt)
print(x)'''
'''
txt = "sdfg@email.ru sdfghjk@kbtu.com"
pattern=r"\w.+@email.ru"
x = re.findall(pattern, txt)
print(x)
'''
'''
txt = "The_rain_in_Spain"
x = re.sub("_","15", txt)
print(x)'''
'''
txt = "The_sdf_dfg_dfg_sdfg"
def snake_to_camel(s):
    parts = s.split('_')
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])
print(snake_to_camel(txt))
'''
'''
text = "SplitAStringAtUppercaseLetters"
parts = re.findall('[A-Z][^A-Z]*', text)
print(parts)
'''
text = "Insert5SpacesBetweenWords6StartingWithCapitalL9etters"
result = re.sub(r"([a-z])([A-Z])([0-9])", r"\1_\2 \3", text)
print(result)

import re

# Example text (string)
text = "Call me at 87071234567 or 87479876543, but not at 123456789."
pattern = r"\b\d{11}\b"
numbers = re.findall(pattern, text)
print("Found phone numbers:", numbers)

text = "ConvertThisCamelCaseToSnakeCase"
result = re.sub(r'(?<!^)(?=[A-Z])', '_', text).lower()
print(result)