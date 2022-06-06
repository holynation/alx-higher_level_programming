#!/usr/bin/python3
def element_at(my_list, idx):
	listCount = len(my_list)
	if idx < 0 or idx > listCount:
		return None
	return my_list[idx]
