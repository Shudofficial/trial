# person = {
#     "name" : "cathy" ,
#     "age" : 23,
#     "pets" : ["dog" , "cat"]
# }

# print(person["pets"])
profile={}

def register():
    username=input("enter username")
    email= input("enter Email")
    password= input("enter password")


# store in directory
    profile["username"]= username
    profile["Email"]= email
    profile["password"]=password

def get_profile():
    print(profile)

def change_username():
    new_username=input("enter new username")
    profile["username"]= new_username


register()
get_profile()

change_username()
get_profile()