def compare_strings(string1, string2):

    sorted1 = sorted(string1)
    sorted2 = sorted(string2)


    if len(sorted1) != len(sorted2):
        return False

    for i in range(len(sorted1)):
        if sorted1[i] != sorted2[i]:
            return False

    return 'yes'

print(compare_strings('abcd', 'cdab'))  # Output: True
print(compare_strings('abcd', 'abtc'))  # Output: False
print(compare_strings('AABC', 'ABC'))   # Output: False
