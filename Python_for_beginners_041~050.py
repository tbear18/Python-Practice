# 041
ticker = "btc_krw"
print(ticker.upper())

# 042
print(ticker.lower())

# 043
string = "hello"
print(string.capitalize())

# 044
file_name = "file.pptx"
print(file_name.endswith("pptx"))

# 045
file_name = "file.pptx"
print(file_name.endswith(("pptx", "ppt")))

# 046
abc = "2020_abcd"
abc = abc.startswith("2020")
print(abc)

# 047
a = "hello world"
print(a.split())

# 048
print(ticker.split("_"))

# 049
date = "2020-07-10"
date.split("-")

# 050
data = "039000      "
data = data.rstrip()
print(data)
# rstrip() 오른쪽 공백이 제거된 새로운 문자열 객체가 반환