"""
At least 8 char long
Contains any sort letters, numbers $%#@
End with a number

"""
import re

pattern = re.compile(r"[A-Za-z0-9$%#@]{8,}\d")
string = 'fsfsfgfgsf#$5%9'
check = pattern.fullmatch(string)

print(check)

