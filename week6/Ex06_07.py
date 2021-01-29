file=open("mangoRecipe.txt", 'r', encoding='utf-8')
lines = file.read()
print(lines)
file.close()    

print("------------")
file=open("mangoRecipe.txt", 'r', encoding='utf-8')
while True:
    line = file.readline()
    if not line:
        break
    print(line, end='') #end='' don't show line end symbol

file.close()    

print("-------------")
file=open("mangoRecipe.txt", 'r', encoding='utf-8')
for line in file.readlines() :
    print(line, end='') #end='' don't show line end symbol

file.close()    
