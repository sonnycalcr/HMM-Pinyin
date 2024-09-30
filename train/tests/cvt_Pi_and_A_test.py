"""
"../../assets/pure_text/data/data_for_A_cvt.txt", "../../assets/pure_text/data/data_for_Pi_cvt.txt" 此二者皆为排序好、归一并取完 log 之后的数据
"""
import os.path
import json


data_for_A_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../assets/pure_text/data/data_for_A_cvt.txt"))
data_for_Pi_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../assets/pure_text/data/data_for_Pi_cvt.txt"))

A_dict: dict[str, dict[str, dict[str, dict[str, int]]]] = {}
Pi_dict: dict[str, dict[str, int]] = {}

with open(data_for_Pi_path, 'rb') as Pi_file:
    Pi_dict_str = Pi_file.read().decode()
    Pi_dict = json.loads(Pi_dict_str)

with open(data_for_A_path, 'rb') as A_file:
    A_dict_str = A_file.read().decode()
    A_dict = json.loads(A_dict_str)

print(Pi_dict.keys())
print(A_dict.keys())
print(len(Pi_dict))
print(len(A_dict))
print(Pi_dict["yi"]["以"])
