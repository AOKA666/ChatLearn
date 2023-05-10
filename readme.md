# 帮你练习英文写作

## 用法

1. `config.py`中填入你的API Key
2. 运行`run.py`
3. `pip install -r requirements.txt `安装依赖
4. 在本地浏览器打开`127.0.0.1:5000`就可以开始练习了，点击“开始练习”之后，后台会自动给出中文，你只需翻译好回复过去就可以了

## 界面

![主界面](https://gitee.com/AOKA666/image-repository/raw/master/images/%E4%B8%BB%E7%95%8C%E9%9D%A2.png)

## 注意

- 不成熟，很简单的一个界面，点击开始练习之后如果没有动静，后台刷新多启动几次，可能网络还不通

- 最好不要问乱七八糟的问题，以免训练数据出现bug

- 如果你想继续训练模型，打开`/app/api/train.py`，单独运行这个脚本，然后输入“开始练习”。对话的内容都会存放在`conversation.db`中，有需要也可以自行修改。

  ![训练界面](https://gitee.com/AOKA666/image-repository/raw/master/images/%E8%AE%AD%E7%BB%83%E7%95%8C%E9%9D%A2.png)

## 最后

本人代码半小白，很多都是chatgpt生成的，如果有问题，我相信各位大手子应该能自己修改的（哈哈哈）
