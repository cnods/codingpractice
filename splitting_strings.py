# Python code below

# Complete function check_strings() to accept two arguments and return True if they are the same

# Parameters first_string, second_string

# Constraints both strings will be non-empty

def check_strings(str1, str2):
    i = 0
    for item in str1:
        if str1[i] == str2[i]:
            i += 1
            if i == len(str1):
                return True        
        else:
            return False



str1 = "Python is fun!"
str2 = "Python is fun!"
str3 = "Python's fun!"
result1 = check_strings(str1, str2)
result2 = check_strings(str2, str3)
print(result1)
print(result2)
