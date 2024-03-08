
approved_users = "elarson,bmoreno,tshah,sgilmore,eraab"
print("before .split():", approved_users)
approved_users = approved_users.split(",")
print("after .split():", approved_users)

removed_users = "wjaffrey jsoto abernard jhill awilliam"
print("before .split():\n", removed_users)
removed_users = removed_users.split()
print("after .split():\n", removed_users) # splting the space


"""

import re

pattern = "\w+:\s\d+"
employee_logins_string = "1001 bmoreno: 12 Marketing 1002 tshah: 7 Human Resources 1003 sgilmore: 5 Finance"
print(re.findall(pattern, employee_logins_string))




print(re.findall("ts", "tsnow, tshah, bmoreno"))
print(re.findall("\d", "h32rb17"))
print(re.findall("\d+", "h32rb17"))
print(re.findall("\d+", "h321rb171"))
print(re.findall("\d*", "h32rb17"))
print(re.findall("\d{2}", "h32rb17 k825t0m c2994eh"))

"""

"""
username_list = ["elarson", "fgarcia", "tshah", "sgilmore"]
print("Before changing an element:", username_list)
username_list[1] = "bmoreno"
print("After changing an element:", username_list)
"""

""" 
def test():
    print('testing function')


test()

tshah_index = "tsnow, tshah, bmoreno - updated".index("tshah")
print(tshah_index)
"""

