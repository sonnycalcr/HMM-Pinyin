import os.path
import json

pure_CHN_text_with_pinyin_verificated_final_path = os.path.abspath(os.path.join(
    os.path.dirname(__file__), "../assets/pure_text/pure_CHN_text_with_pinyin_verificated_final.txt"))

data_for_A_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../assets/pure_text/data/data_for_A.txt"))
# data_for_B_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../assets/pure_text/data/data_for_B.txt"))
data_for_Pi_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../assets/pure_text/data/data_for_Pi.txt"))

data_for_A_path_dir = os.path.dirname(data_for_A_path)
if not os.path.exists(data_for_A_path_dir):
    os.makedirs(data_for_A_path_dir)
if os.path.exists(data_for_Pi_path):
    os.remove(data_for_Pi_path)
if os.path.exists(data_for_A_path):
    os.remove(data_for_A_path)

"""
A_dict e.g. 
{
  "yi": {
    "一": {
      "a": {
        "啊": 11,
        "阿": 12,
        "腌": 8
      },
      "ai": {
        "矮": 11,
        "爱": 12
      },
      "an": {
        "安": 24,
        "案": 18
      }
    },
    "已": {
      "jing": {
        "经": 1032,
        "竟": 32
      }
    }
  },
  "wo": {
    "我": {
      "bu": {
        "不": 123,
        "补": 12
      },
      "tai": {
        "太": 22,
        "抬": 23
      }
    }
  }
}
B_dict e.g. 
Pi_dict e.g. 
{
  "a": 
  {
    "伌": 12,
    "侒": 13,
    "俺": 13,
    "傲": 4,
    "僾": 1,
    "凹": 4,
    "卬": 5,
    "厫": 15
  }, 
  "pai": 
  {
    "俳": 19,
    "哌": 19,
    "廹": 19,
    "徘": 19,
    "拍": 19,
    "排": 19,
    "棑": 19,
    "派": 19,
    "渒": 19,
  }, 
}
"""
A_dict: dict[str, dict[str, dict[str, dict[str, int]]]] = {}  # 转移概率矩阵
# B_dict = {}
Pi_dict: dict[str, dict[str, int]] = {}
with open(pure_CHN_text_with_pinyin_verificated_final_path, "rb") as file, open(data_for_A_path, "wb") as A_file, open(data_for_Pi_path, "wb") as Pi_file:
    count = 0
    for each_line in file:
        cur_line = each_line.decode().strip()
        han_str = cur_line.split(":")[0]
        pinyin_list = cur_line.split(":")[1].split("'")
        index = 0
        for han_char, pinyin_str in zip(han_str, pinyin_list):
            index += 1
            # 先处理 Pi
            if pinyin_str in Pi_dict:
                if han_char in Pi_dict[pinyin_str]:
                    Pi_dict[pinyin_str][han_char] += 1
                else:
                    Pi_dict[pinyin_str][han_char] = 1
            else:
                Pi_dict[pinyin_str] = {han_char: 1}

            # 处理 A
            if index != len(han_str):
                next_han_char, next_pinyin_str = han_str[index], pinyin_list[index]
                if pinyin_str in A_dict:
                    if han_char in A_dict[pinyin_str]:
                        if next_pinyin_str in A_dict[pinyin_str][han_char]:
                            if next_han_char in A_dict[pinyin_str][han_char][next_pinyin_str]:
                                A_dict[pinyin_str][han_char][next_pinyin_str][next_han_char] += 1
                            else:
                                A_dict[pinyin_str][han_char][next_pinyin_str][next_han_char] = 1
                        else:
                            A_dict[pinyin_str][han_char][next_pinyin_str] = {next_han_char: 1}
                    else:
                        A_dict[pinyin_str][han_char] = {next_pinyin_str: {next_han_char: 1}}
                else:
                    A_dict[pinyin_str] = {han_char: {next_pinyin_str: {next_han_char: 1}}}

        count += 1
        if count % 1000000 == 0:
            print(count)
    print(count)

    # 写入文件
    Pi_dict_str = json.dumps(Pi_dict, ensure_ascii=False)
    Pi_file.write(Pi_dict_str.encode())
    A_dict_str = json.dumps(A_dict, ensure_ascii=False)
    A_file.write(A_dict_str.encode())
