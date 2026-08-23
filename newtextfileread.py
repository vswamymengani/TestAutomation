with open("stdemptest.txt",'w') as file:
    file.write("Std_ID : STD_001\n")
    file.write("Std_Name: Raghu\n")
    file.write("student status: applied tc\n")
with open("stdemptest.txt",'r') as file:
    content=file.read()
    print(content)
file_path='stdemptest.txt'
delet_rec="Raghu"
with open('stdemptest.txt','r') as file:
    lines=file.readlines()
with open('stdemptest.txt','w') as file:
    for line in lines:
        if delet_rec not in line:
            outfile=file.write(line)
with open("stdemptest.txt",'r') as file:
    content=file.read()
    print(content)
del_row_num=2
file_path='stdemptest.txt'
with open(file_path,'r') as file:
    lines=file.readlines()
with open(file_path,"w") as file:
    for line_num,line in enumerate(lines,start=1):
        if line_num != del_row_num:
            file.write(line)
with open(file_path,'r') as file:
    content=file.read()
    print(content)
