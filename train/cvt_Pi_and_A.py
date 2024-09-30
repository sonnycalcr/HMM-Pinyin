import os.path
import json
from math import log


data_for_A_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../assets/pure_text/data/data_for_A.txt"))
data_for_Pi_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../assets/pure_text/data/data_for_Pi.txt"))
# sorted and converted data
data_for_A_cvt_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../assets/pure_text/data/data_for_A_cvt.txt"))
data_for_Pi_cvt_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../assets/pure_text/data/data_for_Pi_cvt.txt"))

A_dict: dict[str, dict[str, dict[str, dict[str, int | float]]]] = {}
# B_dict = {}
Pi_dict: dict[str, dict[str, int | float]] = {}

with open(data_for_Pi_path, 'rb') as Pi_file:
    Pi_dict_str = Pi_file.read().decode()
    Pi_dict = json.loads(Pi_dict_str)

with open(data_for_A_path, 'rb') as A_file:
    A_dict_str = A_file.read().decode()
    A_dict = json.loads(A_dict_str)


# sort A_dict
for key_1 in A_dict.keys():
    for key_2 in A_dict[key_1].keys():
        for key_3 in A_dict[key_1][key_2].keys():
            A_dict[key_1][key_2][key_3] = dict(sorted(A_dict[key_1][key_2][key_3].items(), key=lambda item: item[1], reverse=True))
# sort Pi_dict
for key_1 in Pi_dict.keys():
    Pi_dict[key_1] = dict(sorted(Pi_dict[key_1].items(), key=lambda item: item[1], reverse=True))

# 将频次转为 0~1 之间的概率，然后作 log 运算进行归一化处理
# 处理 A_dict
for key_1 in A_dict.keys():
    for key_2 in A_dict[key_1].keys():
        for key_3 in A_dict[key_1][key_2].keys():
            cur_all_cnt = 0
            for value in A_dict[key_1][key_2][key_3].values():
                cur_all_cnt += value
            for key_4 in A_dict[key_1][key_2][key_3]:
                A_dict[key_1][key_2][key_3][key_4] = log(A_dict[key_1][key_2][key_3][key_4] / cur_all_cnt)
# 处理 Pi_dict
for key_1 in Pi_dict.keys():
    cur_all_cnt = 0
    for value in Pi_dict[key_1].values():
        cur_all_cnt += value
    for key_2 in Pi_dict[key_1]:
        Pi_dict[key_1][key_2] = log(Pi_dict[key_1][key_2] / cur_all_cnt)

with open(data_for_A_cvt_path, "wb") as A_cvt_file, open(data_for_Pi_cvt_path, "wb") as Pi_cvt_file:
    # 写入文件
    Pi_dict_str = json.dumps(Pi_dict, ensure_ascii=False)
    Pi_cvt_file.write(Pi_dict_str.encode())
    A_dict_str = json.dumps(A_dict, ensure_ascii=False)
    A_cvt_file.write(A_dict_str.encode())
