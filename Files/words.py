import re

message = 'To be, or not to be, that is the question'
words = re.findall("\w+",message)
print(len(words))