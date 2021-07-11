from read_in import pocket_analysis
res = pocket_analysis("1COZ_info.txt")
# test beginning and end of list
assert res[0][0] == 0.895, "first value extracted from 1COZ_info.txt incorrect"
assert res[4][18] == 0.406, "last value extracted from 1COZ_info.txt incorrect"
res = pocket_analysis("1AO0_info.txt")
# test beginning and end of list again
assert res[0][0] == 0.770, "first value extracted from 1AO0_info.txt incorrect"
assert res[16][18] == 0.629, "last value extracted from 1AO0_info.txt incorrect"
