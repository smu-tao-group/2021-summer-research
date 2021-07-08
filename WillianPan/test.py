from read_in import pocket_analysis
res = pocket_analysis("1COZ_info.txt")
# test beginning and end of list
assert res[0][0] == 0.895, "the first value extracted from 1COZ_info.txt is incorrect"
assert res[4][18] == 0.406, "the last value extracted from 1COZ_info.txt is incorrect"
res = pocket_analysis("1AO0_info.txt")
# test beginning and end of list again
assert res[0][0] == 0.895, "the first value extracted from 1AO0_info.txt is incorrect"
assert res[16][18] == 0.406, "the last value extracted from 1AO0_info.txt is incorrect"
