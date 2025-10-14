import re

# 1. 'a' followed by zero or more 'b's--------------------------------------------------------------------
txt = "ab abb a abbb acb"
print(re.findall(r"ab*", txt))

# 2. 'a' followed by two to three 'b's--------------------------------------------------------------------
txt = "ab abb abbb abbbb a"
print(re.findall(r"ab{2,3}", txt))

# 3. lowercase letters joined with underscore--------------------------------------------------------------------
txt = "this_is_a_test example_string not_valid_123"
print(re.findall(r"[a-z]+_[a-z]+", txt))

# 4. one uppercase letter followed by lowercase letters--------------------------------------------------------------------
txt = "Hello World Test CASE example"
print(re.findall(r"[A-Z][a-z]+", txt))

# 5. 'a' followed by anything, ending in 'b'--------------------------------------------------------------------
txts = ["acb", "a123b", "a_b", "ab", "ax"]
for t in txts:
    if re.fullmatch(r"a.*b", t):
        print(t)

# 6. replace spaces, commas, or dots with a colon--------------------------------------------------------------------
txt = "Python, is. great language"
print(re.sub(r"[ ,.]", ":", txt))

# 7. snake_case → camelCase--------------------------------------------------------------------
txt = "this_is_snake_case"
print(re.sub(r"_([a-z])", lambda x: x.group(1).upper(), txt))

# 8. split string at uppercase letters--------------------------------------------------------------------
txt = "SplitAtUpperCaseLetters"
print(re.findall(r"[A-Z][^A-Z]*", txt))

# 9. insert spaces between capitalized words--------------------------------------------------------------------
txt = "InsertSpacesBetweenWordsStartingWithCapitalLetters"
print(re.sub(r"([a-z])([A-Z])", r"\1 \2", txt))

# 10. camelCase → snake_case--------------------------------------------------------------------
txt = "ConvertThisCamelCaseToSnakeCase"
print(re.sub(r'(?<!^)(?=[A-Z])', '_', txt).lower())
