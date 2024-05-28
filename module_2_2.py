first=15
second=15
third=15
if first==second and second==third:
    print(3)
elif first==second or second==third or first==third:
    print(2)
elif not first==second or second==third or first==third:
    print(0)