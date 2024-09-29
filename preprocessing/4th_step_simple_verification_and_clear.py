"""
对于 step3 中的文字连通块和注音，对其注音进行校验并且丢掉有问题的数据。
"""

import os
import re


def is_alpha(word):
    return bool(re.match('^[a-z]+$', word))


pure_CHN_text_with_pinyin_final_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../assets/pure_text/pure_CHN_text_with_pinyin_final.txt"))
pure_CHN_text_with_pinyin_verificated_final_path = os.path.abspath(os.path.join(
    os.path.dirname(__file__), "../assets/pure_text/pure_CHN_text_with_pinyin_verificated_final.txt"))

if os.path.exists(pure_CHN_text_with_pinyin_verificated_final_path):
    os.remove(pure_CHN_text_with_pinyin_verificated_final_path)
    print("deleted exisited file.")

with open(pure_CHN_text_with_pinyin_verificated_final_path, "wb") as wfile:
    with open(pure_CHN_text_with_pinyin_final_path, "rb") as file:
        count = 0
        for each_line in file:
            cur_line = each_line.decode().strip()
            pinyin_str: str = "".join(cur_line.split(":")[1].split("'"))
            if not (is_alpha(pinyin_str) and pinyin_str.islower()):  # caution! 这里不能使用字符串内置的 isalpha 来判断是否是纯英文字符串，比如，反例：䃟
                # print("error: " + cur_line)
                continue
            wfile.write((cur_line + "\n").encode())
            if count % 100000 == 0:
                print(count)
            count += 1
        print(count)  # 预计：328801419；实际：328795754
