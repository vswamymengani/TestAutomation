###Unstructures text file read and write
#write data in to txt file
with open("accidentfile.text",'w') as file:
    file.write("claimid: CLM9924\n")
    file.write("Adjuster Notes: car hits a building due to heavy rain\n")
    file.write("Status: Pending policy report verification\n")
#Read Data from Txt file
with open("accidentfile.text",'r') as file:
    content=file.read()
    print(content)
#delete a specific line number from text file
file_path="accidentfile.text"
line_delete=0
with open(file_path,'r') as file:
    lines=file.readlines()
with open(file_path,"w") as file:
    for index,line in enumerate(lines,start=1):
        if index!=line_delete:
            file.write(line)
        else:
            print("not line number match to delete")
