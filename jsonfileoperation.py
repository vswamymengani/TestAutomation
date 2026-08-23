import json
# --- WRITING A JSON FILE ---
customer_profile = {
    "policy_number": "POL-7765",
    "holder_name": "Amit Kumar",
    "coverage_type": "Family Floater",
    "insured_members": ["Amit", "Kiran", "Aarav"]
}
with open("profile.json",'w') as file:
    json.dump(customer_profile,file,indent=4)
with open("profile.json",'r') as file:
    data=json.load(file)
    print(data)
    print(f"customer name :{data['holder_name']}")
    print(f"insured family names: {','.join(data['insured_members'])}") 