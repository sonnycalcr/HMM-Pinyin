"""
- 对于 step3 中提取出的文字，这里再行切割，将所有连在一起的汉字块(block，连通块)单独切割出来，然后，分别放在单独的一行。因为，其实一个连通块的开头，其实也可以算是一句话的开头，用来训练 A B Pi 三个数据。

所有的连通块按行写入到文本文件(pure_CHN_text_with_pinyin_verificated_final.txt)中。
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
