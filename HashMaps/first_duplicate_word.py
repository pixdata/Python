 """
 1) Problem Statement : Given a string find the first duplicate word,
 example string: “this is just a wonder, wonder why do I have this in mind”
 
 - The right data-structure to check for existence : 
 Set in Python (order in not preserved) -- NOT HashMap
 """

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
   
string =  "this is just a wonder, wonder why do I have this in mind"
firstduplicate(string)

#-------------------------------------------------------------------

 """
 1) Problem Statement : What if we wanted to find the first word with more than 2 duplicates in a string?
 -  The right data-structure is the HashMap to get access in O(1) in Python, use dict()
 """

def first2timesduplicate(string: str) -> str:
    import re
    cleanStr = re.sub("[^a-zA-Z -]", "", string)

    words = cleanStr.lower().split(" ")
    seen_words = dict()
    for word in words:
        previous_count = seen_words.get(word, 0)
        seen_words[word] = previous_count + 1
        if previous_count >= 2:
            return word
    return None
   
first2timesduplicate(string)


