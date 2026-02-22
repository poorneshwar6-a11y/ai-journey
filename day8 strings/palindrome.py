word=input("enter a word:")
if(word==word[::-1]):
    palindrome=1
else:
    palindrome=0
if(palindrome==1):
    print("The word",word,"is a palindrome")
else:
    print("The word",word,"is not palindrome")
