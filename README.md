# About

`./assets/` 中为训练材料，来自于这个[仓库](https://github.com/brightmart/nlp_chinese_corpus)，仅作一些解压的处理，内容没有改动。

对于 news2016，本项目只用了其中的 `news2016zh_train.json` 这份训练文本。

首先，训练，

- Pi(π): 初始概率。对训练数据的所有内容按照单字分词，并统计每个词出现的频率。
- A: 统计训练数据中每个汉字后面出现的汉字的频率，以此作为隐藏状态的转移概率 A。
- B: 将训练数据的所有汉字都转换成对应的拼音，统计每个拼音对应的汉字以及各自出现的频率，以此作为发射概率 B。


----------

参考：

- 1、<https://gist.github.com/Yukino256/d7e0ed745f282c506a489821813555cc>
- 2、<https://lesley0416.github.io/2019/03/01/HMM_IM/>
- 3、<https://elliot00.com/posts/input-method-hmm>


