new_list = [input(), input(), input(), input(), input(), input()]
new_list[::2], new_list[1::2] = new_list[1::2], new_list[::2]
print(new_list)