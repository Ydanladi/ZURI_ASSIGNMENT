# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    var1= list(word)
    var2 = list(anagram)
    if sorted(word)==sorted(anagram):
        return True
    else:
        return False

var3=find_anagram("creative", "reactive")
print(var3)

