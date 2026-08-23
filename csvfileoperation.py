import csv
policy_data=[
    ["policy_number","holder_name","insure_amt"],
    ["Plcy_001","Raghu","1234.50"],
    ["plcy_002","Priya","3000.00"]]
with open("policy_info.csv",'w',newline="") as file:
    writer=csv.writer(file)
    writer.writerows(policy_data)

with open("policy_info.csv",'r') as file:
    reader=csv.reader(file)
    for lines in reader:
        print(f"policy:{lines[0]} | owner: {lines[1]}")