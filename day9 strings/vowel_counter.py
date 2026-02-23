text =input("enter your text:")
total=0
text1=text.lower()
vowels="aeiou"
consonants=0
for ch in text1:
    if(ch in vowels and ch.isalpha()):
        total+=1
    elif(ch.isalpha() and ch not in vowels):
        consonants+=1
    
print("no. of vowels is:",total)
print("no.of consonants is:",consonants )