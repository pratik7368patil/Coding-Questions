# IVA is a subsequence of OLIVIA (obtained after removal of elements OLIA),
# so Olivia is allowed to keep Iva as a pet and vice versa.
# However, LOONY is not a subsequence of BROOKLYN because the order matters.
# So, Brooklyn is not allowed to keep Loony as a pet and vice versa.
# Given two names, A and B, you need to determine if they form a valid pet-owner pair

# now we have to check for subsequence of first string into second 
# if second string is smaller then first then swap them 

def forever_home(str1 , str2):
    length_str1 = len(str1)
    length_str2 = len(str2)
    
    if length_str2 < length_str1:
        str1, str2 = str2, str1
    
    i = 0 # index for str1
    j = 0 # index for str2
    
    while i < length_str1 and j < length_str2:
        if str2[j] == str1[i]:
            i += 1
        j += 1
    return i == length_str1
    
str1 = "IVA"
str2 = "OLIVIA"

print(forever_home(str1, str2))

## complexity of this program is O(max(lenght_str1 , length_str2)))