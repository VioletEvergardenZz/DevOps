# 处理正则表达式的标准库
import re

text = "The quick brown fox"
# 正则表达式模式字符串 该模式是要在文本中搜索的内容
# 原始字符串(raw string) 转义字符会被直接量解析而不是被转义
pattern = r"brown"

search = re.search(pattern, text)
if search:
    # search.group() 将返回与模式匹配的实际文本
    print("Pattern found:", search.group())
else:
    print("Pattern not found")