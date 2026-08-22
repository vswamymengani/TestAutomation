"""*args & **kwargs concepts"""
def sum_of_total(*args):
    print(f"received args {args}")
    return sum(args)
Total=sum_of_total(5,10,15,2)
print("Total values:",Total)
def student_profile(**kwargs):
    print(f"received arguments")
    for key,value in kwargs.items():
        print(f"{key}: {value}")
student_profile(student_Name="Amit",Class="9th B")
def master_function(req_arg,*args,default_args="Venkat",**kwargs):
    print("Required arguments are",req_arg)
    print("*args are",args)
    print("default args are:",default_args)
    print("kewword args:",kwargs.items())
    for key,value in kwargs.items():
        print(f"kewword args:{key}:{value}")
master_function("Hello",1,2,3,4,default_args="Swamy",city="hyderabad",pin=500086)