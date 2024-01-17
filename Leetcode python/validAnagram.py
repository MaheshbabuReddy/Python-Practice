def is_anagram(s1,s2):
    return set(s1) == set(s2)
s1="low"
s2="owl"
if is_anagram(s1,s2) == True:
    print("It is Anagram")

