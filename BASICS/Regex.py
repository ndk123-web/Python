import re 

txt =  "apple banana Apple BANANA"

# 1 # search return str
pattern = r"apple"
chk = re.search(pattern,txt)
print("USING SEARCH",chk.group())

    # """ . (dot) matches any character except newline.
    #     ^ asserts the start of a string.
    #     $ asserts the end of a string.
    # """
    
# 2 # Match return str
pattern = r"^apple"
chk = re.match(pattern,txt)
print("USING MATCH",chk.group())

    # """ \d for digits (0-9).
    #     \w for word characters (letters, digits, and underscores).
    #     \s for whitespace characters (spaces, tabs).
    # """

# 3 # Findall return lists
pattern = r"\d{3}"
text = "123 456 78"
matches = re.findall(pattern, text)
print(matches) 

    # """ * Zero or more times.
    #     + One or more times.
    #     ? Zero or one time.
    #     {n} Exactly n times.
    #     {n,} At least n times.
    #     {n,m} Between n and m times.
    # """

txt = "123 3456"
pattern = r"\d{2,4}"
matchs = re.findall(pattern,txt)
print(matchs)

# 4 # Grouping and Capturing
txt = "123-45-6789"
pattern=r"(\d{3})-(\d{2})-(\d{4})"
m = re.match(pattern,txt)
print(m.group(1))
print(m.group(2))
print(m.group(3))