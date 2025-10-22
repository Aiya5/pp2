'''
findall("patterns", txt)
sub("patterns", txt)
re.split("\s", txt)
fullmatch(pattern,txt)
"ab*"
"ab{2,3}"
"[a-z]+_[a-z]+"
"[A-Z][a-z]+"
"a.*b"
"[ ,.]"
'[A-Z][^A-Z]*'
([a-z])([A-Z])"
he..o- any two characters
he.+o"- one or more characters
he.?o- zero or one occurence
he.{2}o- exactly two cgaracters
"falls|stay- or
"\s" — means any whitespace character
\d- digits
\w	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)
\b	Returns a match where the specified characters are at the beginning or at the end of a word
^	    Start of the string	Match must begin with what follows
The	    The exact text "The"	Match starts with this word
.*	    Any characters, any number of times (even none)	. = any character, * = zero or more
Spain	The exact text "Spain"	Match ends with this word
$	    End of the string	Match must end here
'''