# file open in write mode if does not exite create and open file for writting and if exite  truncate it and open for write
# f = open("./Practice/myfile.txt","w")
# for write single line
# f.write("line by write\n")

# for write multiple lines
# lines=["line by writelines line 2 \n","line 2 \n","line 2 \n"]
# f.writelines(lines)
# f.close()

######################

# open file in read mode for reading file
# f = open("./Practice/myfile.txt","r")
# read file file
# line = f.read()
# print file text 
# print(line)

# lines = f.readlines()
# print(lines)
# l=0
# i=0
# for line in lines:
#     line = line.split(",")
#     l = len(line)+l
#     nm = line[0]
#     m1 = int(line[1])
#     m2 = int(line[2])
#     m3 = int(line[3])
#     total = m1+m2+m3
#     i += 1
    # print(line)
#     print(f"Marks of {i}th Student {nm} : {m1} + {m2} + {m3}  Total: {total}")

# print("total no of lines in file ", i)
# print("count no of Words in file ", l)
# f.close()

#######################

## write text and read it 

# text = input("Enter text : ")
# f = open("./Practice/myfile.txt","w")
# f.write(text)
# f.close()
# f = open("./Practice/myfile.txt","r")
# line = f.read()
# print(line)
# f.close()

#################

### Apend text in file

# f = open("./Practice/myfile.txt","a")
# apend = f.write("last\n")
# f.close()
# f = open("./Practice/myfile.txt","r")
# line = f.read()
# print(line)
# f.close()