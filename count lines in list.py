a = [7, 10] # One unit
#a = [4,5, 20, 34,35, 50, 78,80] # Five units
#a = [1, 10, 30,31, 80] # Four units

def count_lines(list, min_new_list):
	len_list = len(list)
	new_list, units = [], 0

	for item in range(len(list)-1):
		actual = list[item]
		after = list[item+1]
		new_list.append(after-actual)

	if len_list == 1:
		units = 1
	elif len_list == 2:
		if new_list[0] < min_new_list:
			units = 1
		else:
			units = 2
	else:
		units = len([1 for i in new_list if i > min_new_list]) + 1

	return units

units = count_lines(a, 5)
print('Units:', units)