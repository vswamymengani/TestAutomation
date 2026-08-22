#reading a file
try:
    file_path="C:/Users/Admin/Downloads/QA Automation guid.txt"
    with open(file_path,'r',encoding='cp1252') as file:
        connect=file.read()
        print(connect)
except FileNotFoundError:
    print("file not found")
except Exception as e:
    print(f"\n[AN UNEXPECTED ERROR OCCURRED]: {e}")
else:
    print("success")
finally:
    print("close the file")