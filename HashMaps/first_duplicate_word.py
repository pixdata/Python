 Problem Statement : Given a string find the first duplicate word,
 example string: “this is just a wonder, wonder why do I have this in mind”
 
 
 
 - The right data-structure to check for existence : 
  set in Python (order in not preserved)
  

```
string = "this is just a wonder, wonder why do I have this in mind"
def firstduplicate(string: str) -> str:
    import re
    cleanStr = re.sub("[^a-zA-Z -]", "", string)
    
    words = cleanStr.lower().split(" ")
    seen_words = set()
    for word in words:
        if word in seen_words:
            return word
        else: 
            seen_words.add(word)
    return None
firstduplicate(string)

```
