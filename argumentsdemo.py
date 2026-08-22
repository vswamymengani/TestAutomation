def sum_of_total(*args):
    print(f"received args {args}")
    return sum(args)
Total=sum_of_total(5,10,15,2)
print("Total values:",Total)