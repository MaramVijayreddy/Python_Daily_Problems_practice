s = "pwwkiorrew"


# using set

seen=set()
left=0
max_len=0
for right in range(len(s)):
    char=s[right]
    while char in seen:
        seen.remove(s[left])
        left+=1
    seen.add(s[right])
    max_len=max(max_len,right-left+1)
print(max_len)


# using hashmap
# left=0
# max_len=0
# seen={}
# for right in range(len(s)):
#     char=s[right]
#     if char in seen and seen[char]>=left:
#         left=seen[char]+1
#     seen[char]=right
#     curr_len=right-left+1
#     max_len=max(max_len,curr_len)
# print(max_len)
