string=input("Enter string: ")
vowels='aeiouAEIUO'
count=0
for i in string:
    if(i in vowels):
        count+=1
print("Number of vowels in the string:", count)