# COMP411Script

> English Ver
A Script used to auto-check COMP 411 Homework when done. 

Automatically compiles all .c files to executable files, 
and executes "compare commands" - such as `./ex1 < ex1in1 > ex1result1` - automatically.

Prints "file1 match file2" if `diff file1 file2` returns 0 - i.e., two files are identical;

Otherwise prints "Output doesn't match expected in file file1 : file2".

Download **main.py** to the required folder
and run it by typing `$ python3 main.py`
or `$ python main.py` depending on your Operation System.

### Required Modules
1. re
2. os
* * *
> 中文版本
用于自动运行命令的脚本

自动编译gcc并且自动diff。

如果两个文件不一样则输出“Output doesn't match expected in file file1 : file2”

否则返回“file1 match file2”

下载**main.py**到指定文件夹并且在命令行输入`$ python3 main.py`或者`$ python main.py`来运行
执行命令取决于你的操作系统。

### 需要的模块
1. re
2. os

*编写共耗时2小时*
