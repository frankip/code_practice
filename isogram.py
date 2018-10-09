"""
An isogram is a word that has no repeating letters, consecutive or 
non-consecutive. Implement a function that determines whether a string 
that contains only letters is an isogram. Assume the empty string is 
an isogram. Ignore letter case.
"""

def is_isogram(string):
    """
    checks whether a string is an isogram
    """
    
    # convert to the string to lower case
    string = string.lower()
    if string == "":
        return True
    return len(set(string)) == len(string)
    