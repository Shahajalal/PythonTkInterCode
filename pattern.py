str="1000.0"
index=str.find(".")
print(index)
if(str[index+1:]=="0"):
    print(str[:index-1])
else:
    print(str)