"""
- 对于 step1 中提取出的文字，这里再行切割，将所有连在一起的汉字块(block，连通块)单独切割出来，然后，分别放在单独的一行。因为，其实一个连通块的开头，其实也可以算是一句话的开头，用来训练 A B Pi 三个数据。

所有的连通块按行写入到文本文件(pure_CHN_text_final.txt)中。
"""

import os.path
import regex as re
from pypinyin import lazy_pinyin

pure_CHN_text_final_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../assets/pure_text/pure_CHN_text_final.txt"))
pure_CHN_text_with_pinyin_final_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../assets/pure_text/pure_CHN_text_with_pinyin_final.txt"))


def extract_chinese_blocks(text):
    # 匹配连续的中文字符块
    chinese_blocks = re.findall(r"[\p{Han}]+", text)
    return chinese_blocks


with open(pure_CHN_text_with_pinyin_final_path, "wb") as wfile:
    with open(pure_CHN_text_final_path, "rb") as file:
        all_lines = file.readlines()
        count = 0
        for each_line in all_lines:
            cur_line = each_line.decode().strip()
            if len(cur_line) == 0:
                continue
            cur_pinyin_list = lazy_pinyin(cur_line)
            cur_pinyin_list_string = "'".join(cur_pinyin_list)
            if (len(cur_line) != len(cur_pinyin_list)):
                # 解决 lazy_pinyin 的特定问题
                if (cur_line == "李祖原觉得当代的社会⼀直讲究⻄⽅的科学"):
                    cur_pinyin_list = ['li', 'zu', 'yuan', 'jue', 'de', 'dang', 'dai', 'de', 'she', 'hui', 'yi', 'zhi', 'jiang', 'jiu', 'xi', 'fang', 'de', 'ke', 'xue']
                    cur_pinyin_list_string = "'".join(cur_pinyin_list)
                else:
                    # 无法标注的就直接跳过吧
                    print("error when using lazy_pinyin to add pinyin for:" + cur_line)
                    continue
            wfile.write((cur_line + ":" + cur_pinyin_list_string + "\n").encode())
            count += 1
            if count % 10000 == 0:
                print(count)
        print(count) # 328801419

"""
❯ wc -l pure_CHN_text_final.txt
328915598 pure_CHN_text_final.txt
HMM-Pinyin/assets/pure_text on  master [✘!?] via 🐍 v3.12.6 (env) 
❯ wc -l pure_CHN_text_with_pinyin_final.txt 
328801419 pure_CHN_text_with_pinyin_final.txt
共有 328915598 - 328801419 = 114179 条数据被略去。
"""

