"""
- 对于 "../assets/news2016/news2016zh_train.json"，对于其中的每一条数据，只取 title 和 content 两个字段。
- 对于 "../assets/wiki_zh_2019/" 中所有的文件，对于其中的每一条数据，只取 text 这个字段。

然后，把这些字段按行写入到新的文本文件(pure_text_final.txt)中。
"""

import json
import os.path


def get_all_files(directory):
    file_paths = []
    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            file_paths.append(os.path.join(dirpath, filename))

    return file_paths


wiki_zh_2019_paths_list = get_all_files(os.path.abspath(os.path.join(os.path.dirname(__file__), "../assets/wiki_zh_2019/")))
wiki_zh_2019_paths_list.sort()
news2016zh_train_json_path = os.path.join(os.path.dirname(__file__), "../assets/news2016/news2016zh_train.json")
output_pure_text_path = os.path.join(os.path.dirname(__file__), "../assets/pure_text/pure_text.txt")
output_pure_text_final_path = os.path.join(os.path.dirname(__file__), "../assets/pure_text/pure_text_final.txt")

output_pure_text_dir = os.path.dirname(output_pure_text_path)

if not os.path.exists(output_pure_text_dir):
    os.makedirs(output_pure_text_dir)
if os.path.exists(output_pure_text_path):
    os.remove(output_pure_text_path)
if os.path.exists(output_pure_text_final_path):
    os.remove(output_pure_text_final_path)

with open(output_pure_text_path, "wb") as wfile:
    # 处理 wiki_zh_2019
    count = 0
    for each_path in wiki_zh_2019_paths_list:
        with open(each_path, "rb") as file:
            all_lines = file.readlines()
            for each_line in all_lines:
                cur_line = each_line.decode().strip()
                if len(cur_line) == 0:
                    continue
                data = json.loads(cur_line)
                wfile.write((data["text"].strip() + "\n").encode())
                count += 1
    print(count)

    # 处理 news2016zh_train
    count = 0
    with open(news2016zh_train_json_path, "rb") as file:
        all_lines = file.readlines()
        for each_line in all_lines:
            cur_line = each_line.decode().strip()
            if len(cur_line) == 0:
                continue
            data = json.loads(cur_line)
            wfile.write((data["title"].strip() + "\n").encode())
            wfile.write((data["content"].strip() + "\n").encode())
            count += 2
    print(count)


with open(output_pure_text_final_path, "wb") as wfile:
    with open(output_pure_text_path, "rb") as file:
        all_lines = file.readlines()
        count = 0
        for each_line in all_lines:
            cur_line = each_line.decode().strip()
            if len(cur_line) == 0:
                continue
            wfile.write((cur_line + "\n").encode())
            count += 1
        print(count)


if os.path.exists(output_pure_text_path):
    os.remove(output_pure_text_path)

