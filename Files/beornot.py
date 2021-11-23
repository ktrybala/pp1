import re

message = 'To be, or not to be, that is the question'
vowels = re.findall("[aeiouy]",message)
print(len(vowels))