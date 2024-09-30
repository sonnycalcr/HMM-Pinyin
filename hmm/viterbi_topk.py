import os.path
import json


data_for_A_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../assets/pure_text/data/data_for_A.txt"))
# data_for_B_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../assets/pure_text/data/data_for_B.txt"))
data_for_Pi_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../assets/pure_text/data/data_for_Pi.txt"))

A_dict: dict[str, dict[str, dict[str, dict[str, int]]]] = {}
# B_dict = {}
Pi_dict: dict[str, dict[str, int]] = {}

with open(data_for_Pi_path, 'rb') as Pi_file:
    Pi_dict_str = Pi_file.read().decode()
    Pi_dict = json.loads(Pi_dict_str)

with open(data_for_A_path, 'rb') as A_file:
    A_dict_str = A_file.read().decode()
    A_dict = json.loads(A_dict_str)


def sort_inner_dict(d):
    for key, value in d.items():
        if isinstance(value, dict):
            # 如果还不是最内层，递归调用
            sort_inner_dict(value)
        # 如果是最内层 dict[str, int]，则对其按值降序排序
        if all(isinstance(v, int) for v in value.values()):
            d[key] = dict(sorted(value.items(), key=lambda item: item[1], reverse=True))


# sort A_dict
for key_1 in A_dict.keys():
    for key_2 in A_dict[key_1].keys():
        for key_3 in A_dict[key_1][key_2].keys():
            A_dict[key_1][key_2][key_3] = dict(sorted(A_dict[key_1][key_2][key_3].items(), key=lambda item: item[1], reverse=True))
# sort Pi_dict
for key_1 in Pi_dict.keys():
    Pi_dict[key_1] = dict(sorted(Pi_dict[key_1].items(), key=lambda item: item[1], reverse=True))

# print(A_dict["yi"]["一"]["ge"])
# print(Pi_dict["pai"])



# print(Pi_dict["yi"])
# print(len(A_dict))
# print(len(Pi_dict))
# print(Pi_dict.keys())
# print(A_dict.keys())
# print(len(Pi_dict))
# print(len(A_dict))

# def viterbi_top_k(quanpin_str: str, Pi: dict[str, dict[str, int]], A: dict[str, dict[str, dict[str, dict[str, int]]]], k: int):
#     if len(quanpin_str) == 0:
#         return ""
#     quanpin_list = quanpin_str.split("'")
#      len(Pi_dict[quanpin_list[0]])

print(Pi_dict["shi"])
print(list(A_dict["shi"]["石"]["you"])[:2])
print(list(A_dict["shi"]["是"]["you"])[:2])

# 是有 是由

# print(Pi_dict["jiang"])
print(list(A_dict["han"]["汉"]["shi"]))
# print(list(A_dict["jiang"]["江"]["shi"])[:2])
# 江汉石油 => 概率 => jiang'han'shi'you
# 江汉油田
# 三个字以内 => 完全搜索
# 其他情况: 
# topk => 100 => N


