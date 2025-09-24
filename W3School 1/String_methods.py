#Python - String Methods

#capitalize()
txt = "hello, and welcome to my world."
x = txt.capitalize()
print (x)    

#casefold()--------------------------------------------------------------------------------
txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)      #Converts string into lower case

#center()-------------------------------------------------------------------------------
txt = "banana"
x = txt.center(20)
print(x)            	#Returns a centered string

#count()--------------------------------------------------------------------------------------
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)

#encode()---------------------------------------------------------------------------------
txt = "My name is Ståle"
x = txt.encode()
print(x)   #Returns an encoded version of the string

#endswith()------------------------------------------------------------------------------------
txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)      # Returns true if the string ends with the specified value

#expandtabs()-----------------------------------------------------------------------------
txt = "H\te\tl\tl\to"
x =  txt.expandtabs(2)
print(x)         	#Sets the tab size of the string

#find()-------------------------------------------------------------------------------------------
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)    #Searches the string for a specified value and returns the position of where it was found

#format()----------------------------------------------------------------------------------------
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

#format_map()	Formats specified values in a string

#index()---------------------------------------------------------------------------------------
txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x)   #Searches the string for a specified value and returns the position of where it was found

#isalnum()--------------------------------------------------------------------------
txt = "Company12"
x = txt.isalnum()
print(x)   #Returns True if all characters in the string are alphanumeric

#isalpha()-------------------------------------------------------------------------------
txt = "CompanyX"
x = txt.isalpha()
print(x)   #Returns True if all characters in the string are in the alphabet

#isascii()-------------------------------------------------------------------------------
txt = "Company123"
x = txt.isascii()
print(x)   #Returns True if all characters in the string are ascii characters

#isdecimal()------------------------------------------------------------------------------
txt = "1234"
x = txt.isdecimal()
print(x)    #Returns True if all characters in the string are decimals


#isdigit()---------------------------------------------------------------------------
txt = "50800"
x = txt.isdigit()
print(x)   #Returns True if all characters in the string are digits

#isidentifier()-------------------------------------------------------------------
txt = "Demo"
x = txt.isidentifier()
print(x)    #	Returns True if the string is an identifier

#islower()--------------------------------------------------------------------------------
txt = "hello world!"
x = txt.islower()
print(x)   #Returns True if all characters in the string are lower case

#isnumeric()------------------------------------------------------------------------------
txt = "565543"
x = txt.isnumeric()
print(x)    #Returns True if all characters in the string are numeric

#isprintable()-----------------------------------------------------------------------------
txt = "Hello! Are you #1?"
x = txt.isprintable()
print(x)   #Returns True if all characters in the string are printable

#isspacce()-------------------------------------------------------------------------------
txt = "   "
x = txt.isspace()
print(x)   #Returns True if all characters in the string are whitespaces

#istitle()----------------------------------------------------------------------------------
txt = "Hello, And Welcome To My World!"
x = txt.istitle()
print(x)   #Returns True if the string follows the rules of a title


#isupper()------------------------------------------------------------------------------------------
txt = "THIS IS NOW!"
x = txt.isupper()
print(x)   #Returns True if all characters in the string are upper case

#join()---------------------------------------------------------------------------------------
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x) #Joins the elements of an iterable to the end of the string


#ljust()----------------------------------------------------------------------------------------
txt = "banana"
x = txt.ljust(20)
print(x, "is my favorite fruit.")  #Returns a left justified version of the string

#lower()----------------------------------------------------------------------------------
txt = "Hello my FRIENDS"
x = txt.lower()
print(x)    #Converts a string into lower case

#lstrip()-------------------------------------------------------------------------------
txt = "     banana     "
x = txt.lstrip()
print("of all fruits", x, "is my favorite") #Returns a left trim version of the string

#maketrans()---------------------------------------------------------------------------
txt = "Hello Sam!"
mytable = str.maketrans("S", "P")
print(txt.translate(mytable))    #Returns a translation table to be used in translations

#partition()-----------------------------------------------------------------------------
txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x)     #Returns a tuple where the string is parted into three parts

#replace()---------------------------------------------------------------------------------
txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)   #Returns a string where a specified value is replaced with a specified value

#rfind()------------------------------------------------------------------------------------------
txt = "Mi casa, su casa."
x = txt.rfind("casa")
print(x)    #Searches the string for a specified value and returns the last position of where it was found

#rindex()----------------------------------------------------------------------------------
txt = "Mi casa, su casa."
x = txt.rindex("casa")
print(x)     #Searches the string for a specified value and returns the last position of where it was found

#rjust()-------------------------------------------------------------------------------------
txt = "banana"
x = txt.rjust(20)
print(x, "is my favorite fruit.") #Returns a right justified version of the string

#rpartition()--------------------------------------------------------------------------
txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("bananas")
print(x) #Returns a tuple where the string is parted into three parts

#rsplit()---------------------------------------------------------------------------------
txt = "apple, banana, cherry"
x = txt.rsplit(", ")
print(x)  #Splits the string at the specified separator, and returns a list


#rstrip()---------------------------------------------------------------------------
txt = "     banana     "
x = txt.rstrip()
print("of all fruits", x, "is my favorite")    #Returns a right trim version of the string

#split()-------------------------------------------------------------------------------
txt = "welcome to the jungle"
x = txt.split()
print(x)   #Splits the string at the specified separator, and returns a list

#splitlines()---------------------------------------------------------------------------
txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines()
print(x)     #Splits the string at line breaks and returns a list

#startswith()--------------------------------------------------------------------
txt = "Hello, welcome to my world."
x = txt.startswith("Hello")
print(x)   #Returns true if the string starts with the specified value

#strip()-----------------------------------------------------------------------
txt = "     banana     "
x = txt.strip()
print("of all fruits", x, "is my favorite")    #Returns a trimmed version of the string

#swapcase()---------------------------------------------------------------------
txt = "Hello My Name Is PETER"
x = txt.swapcase()
print(x)

#title()-----------------------------------------------------------------------
txt = "Welcome to my world"
x = txt.title()
print(x)     #Converts the first character of each word to upper case

#translate()-----------------------------------------------------------------
#use a dictionary with ascii codes to replace 83 (S) with 80 (P):
mydict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(mydict))

#upper()----------------------------------------------------------------------
txt = "Hello my friends"
x = txt.upper()
print(x)   #Converts a string into upper case

#zfill()------------------------------------------------------------------------
txt = "50"
x = txt.zfill(10)
print(x) #Fills the string with a specified number of 0 values at the beginning