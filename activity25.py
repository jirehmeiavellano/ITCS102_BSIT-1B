
# Dictonary

programming_language = ['Java', 'C#', 'C++','Python', 'Perl', 'Javascript']
# index                    0     1     2        3       4           5

print(programming_language[4])

proglang_dictionary = {'hard':'Java', 'easy':'C#', 'extremely hard':'C++', 'just alright':'Python', 'outdated':'Perl', 'for web':'JavaScript'}

print(proglang_dictionary['just alright'])

# adding item to a dictionary
proglang_dictionary['for beginners'] = 'html'

print(proglang_dictionary)

# deleting item to a dictionary
proglang_dictionary.pop('for beginners')

print(proglang_dictionary)