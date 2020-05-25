x=input(" enter first string:")
y=input("enter second string:")
if(sorted(x)==sorted(y)):
    print(f"strings are anagram")
else:
    print(f"not anagram")