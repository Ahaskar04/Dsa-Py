# Reverse a string 
def reverse(strng):
    if len(strng) == 0: return ''
    else: return strng[-1] + reverse(strng[0:-1])