curr = s[0]
longest = s[0]
max_length = 1
for i in range(1, len(s)):
    if s[i - 1] <= s[i]:
        curr += s[i]
        if len(curr) > max_length:
            max_length = len(curr)
            longest = curr
    else:
        curr = s[i]
print('Longest substring in alphabetical order is:', longest)