with open('file.txt') as f:
    lines = f.readlines()

# line=lines[0].strip('\n')
# print(line)
print(len(lines))
print(lines[0])

for i in range(len(lines)):
   
    line=lines[i].strip('\n')
    for char in range(len(line)):
        if line[char]=='x':
            print('tile')
        if line[char]==' ':
            print("space")



# print(len(lines[0]))
# print(lines[0][0])