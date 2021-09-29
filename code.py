testString = "aaabbccaa";  
string_list = list(testString)
duplicateArray = [0] * 10
print("Duplicate characters in a given string: ");  
#Counts each character present in the string  
for i in range(0, len(testString)):  
    # count = 1;  
    for j in range(i+1, len(testString)):  
        if(testString[i] == testString[j] ):  
            print(testString[i])
            break
    string_list[i] = "0"
            