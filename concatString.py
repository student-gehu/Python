def concat_and_length(str1,str2):
    concat_str=str1+str2
    length_of_str=len(concat_str)
    return concat_str,length_of_str


str1=input("Enter the first string:")
str2=input("Enter the second string:")

concatenated_str,length_of_str=concat_and_length(str1,str2)

print("concatenated string:",concatenated_str)
print("length of concantenated string:",length_of_str)