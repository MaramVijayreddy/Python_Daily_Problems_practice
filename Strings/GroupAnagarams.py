strs = ["eat","tea","tan","ate","nat","bat"]
group={}
for word in strs:
    key="".join(sorted(word))
    if key not in group:
        group[key]=[]
    group[key].append(word)
print(list(group.values()))
