name = input()
count_z = 0
count_o = 0
for i in name:
    if i == 'z':
        count_z += 1
    if i == 'o':
        count_o += 1
if count_z * 2 == count_o:
    print('Yes')
else:
    print('No') 
