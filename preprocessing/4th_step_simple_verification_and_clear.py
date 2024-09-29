"""
对于 step3 中的文字连通块和注音，对其注音进行校验并且丢掉有问题的数据。
"""

import os.path

pure_CHN_text_with_pinyin_final_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../assets/pure_text/pure_CHN_text_with_pinyin_final.txt"))
pure_CHN_text_with_pinyin_verificated_final_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../assets/pure_text/pure_CHN_text_with_pinyin_verificated_final.txt"))

with open(pure_CHN_text_with_pinyin_verificated_final_path, "wb") as wfile:
    with open(pure_CHN_text_with_pinyin_final_path, "rb") as file:
        all_lines = file.readlines()
        count = 0
        for each_line in all_lines:
            cur_line = each_line.decode().strip()
            pinyin_str: str = "".join(cur_line.split(":")[1].split("'"))
            if not ((pinyin_str.isalpha) and (pinyin_str.islower())):
                print("error: " + cur_line)
                continue
            wfile.write((cur_line + "\n").encode())
            if count % 100000 == 0:
                print(count)
            count += 1
        print(count)  # 预计：328801419；实际：328801084
