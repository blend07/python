# def format_name(first_name, last_name):
#     full_name = first_name.title() + " " + last_name.title()
#     return full_name

# print(format_name("John","Doe"))

def get_fullname(first_name: str, last_name: str):
    fullname= first_name.title() + " " + last_name.title()
    return fullname

print(get_fullname("John","Doe"))

def getitems(item_a: str, item_b: int, item_c:float, item_d: bool, item_e:bytes):
    return item_a,item_b,item_c,item_d,item_e

print(get_fullname)