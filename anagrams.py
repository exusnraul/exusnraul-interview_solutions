data = ['eat', 'ate', 'tea', 'ant', 'tan',
        'bat', 'adobe', 'abode', 'listen', 'silent']


data = ['eat', 'ate', 'tea', 'ant', 'tan',
        'bat', 'adobe', 'abode', 'listen', 'silent']
 
 
def createAnagramKey(string):
    key = ''
    for ch in sorted(string):
        key += ch
    print(key)
    return str(key)
 
 
def groupAnagramWords(data):
    group = dict()
    for ele in data:
        if group.get(createAnagramKey(ele)) == None:
            group[createAnagramKey(ele)] = [ele]
        else:
            group[createAnagramKey(ele)].append(ele)
    print(group)
    return group
 
 
anagram_grouped = groupAnagramWords(data)
 
# Anagram in dictonry format
print('In dictonry format')
print(anagram_grouped)
 
anagram_grouped_list = list()
 
for k, v in anagram_grouped.items():
    anagram_grouped_list.append(v)
print('In list format')
print(anagram_grouped_list)