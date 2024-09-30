import os.path
import json


data_for_Pi_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../assets/pure_text/data/data_for_Pi.txt"))

Pi_dict: dict[str, dict[str, int]] = {}

with open(data_for_Pi_path, 'rb') as Pi_file:
    Pi_dict_str = Pi_file.read().decode()
    Pi_dict = json.loads(Pi_dict_str)

# print(Pi_dict["yi"])
# print(len(A_dict))
# print(len(Pi_dict))
# print(Pi_dict.keys())
# print(len(Pi_dict))

max_len = 0
min_len = 10000
for each_key in Pi_dict.keys():
    cur_len = len(Pi_dict[each_key])
    max_len = cur_len if cur_len > max_len else max_len
    min_len = cur_len if cur_len < min_len else min_len

print(max_len)
print(min_len)

