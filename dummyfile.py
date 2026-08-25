with open("stdemptest.txt",'r') as file1:
    data1=file1.readlines()
    for rows in data1:
        print(rows.strip())
print("-----------")
with open("testfile.txt",'r') as file2:
    data2=file2.readlines()
    for rows in data2:
        print(rows.strip())
with open("stdemptest.txt",'w') as file3:
    for rows3 in data2:
        file3.writelines(rows3.strip())
print("-----------")
with open("stdemptest.txt",'r') as filex:
    datax=filex.readlines()
    print(datax)
    print("-----------")
with open("stdemptest.txt",'r') as filey:
    datay=filey.read()
    print(datay)
    print("-----zrec------")
with open("stdemptest.txt",'r') as filez:
    dataz=filez.readlines()
    for rowsz in dataz:
        print(rowsz)