
input_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in input_list:
if i < 5:
print(i)


cut_off = int(input("Please input the cut off number:"))
new_list = [i for i in input_list if i < cut_off]
print(new_list)