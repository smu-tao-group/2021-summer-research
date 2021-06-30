from read_in import pocket_analysis
res = pocket_analysis("1COZ_info.txt")
print(res)
# test beginning and end of list
assert res[0][0] == 0.895
assert res[4][18] == 0.406