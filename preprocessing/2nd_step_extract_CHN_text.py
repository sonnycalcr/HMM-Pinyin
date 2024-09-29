"""
- 对于 step1 中提取出的文字，这里再行切割，将所有连在一起的汉字块(block，连通块)单独切割出来，然后，分别放在单独的一行。因为，其实一个连通块的开头，其实也可以算是一句话的开头，用来训练 A B Pi 三个数据。

所有的连通块按行写入到文本文件(pure_CHN_text_final.txt)中。
"""

import os.path
import regex as re

pure_text_final_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../assets/pure_text/pure_text_final.txt"))
pure_CHN_text_final_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../assets/pure_text/pure_CHN_text_final.txt"))


def extract_chinese_blocks(text):
    # 匹配连续的中文字符块
    chinese_blocks = re.findall(r"[\p{Han}]+", text)
    return chinese_blocks


with open(pure_CHN_text_final_path, "wb") as wfile:
    with open(pure_text_final_path, "rb") as file:
        all_lines = file.readlines()
        count = 0
        for each_line in all_lines:
            cur_line = each_line.decode().strip()
            if len(cur_line) == 0:
                continue
            chn_char_block_list = extract_chinese_blocks(cur_line)
            chn_char_block_list_string = "\n".join(extract_chinese_blocks(cur_line))
            wfile.write((chn_char_block_list_string + "\n").encode())
            count += 1
        print(count)
