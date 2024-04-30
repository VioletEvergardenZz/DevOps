import re

text = "The quick brown fox"
pattern = r"quick"

# 只匹配字符串的开头
match = re.match(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match")