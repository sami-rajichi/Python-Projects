print("ISIMA : Institut Superieur d'Informatique de Mahdia")
print("SamiRajichi")
print("LCS 1 A")

# otherwise, we could stock all of these informations in one variable through triple quotes

s = """ISIMA : Institut Superieur d'Informatique de Mahdia
SamiRajichi
LCS 1 A
"""
print(s)

name = " Sami RAJICHI "
print(name)
print(name[0:5]) # the second parameter represents the length of wanted sequence -1
print(name.strip()) # this function deletes spaces in the end and in the beginning of string
print(name.lower()) # this function converts each character of the string to lower characters
print(name.upper()) # this function converts each character of the string to upper characters
print(name.replace(" RAJICHI",".R")) # this function replaces the string or sequence of string into wanted one
print(name.split(" ")) # it's a helpful function as it splits up the string into words in a list throughout a character chosen by you 