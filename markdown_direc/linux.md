##cat / more / less
###cat(cat命令是整个文件的内容从上到下显示在屏幕上。还可以将多个文件连接起来显示，它常与重定向符号配合使用，适用于文件内容少的情况)
- cat一次展示整个文件 cat
- cat创建一个文件 cat > filename
- 将几个文件合并为一个文件 cat file1 file2 > file3
##### cat [-AbeEnstTuv] [--help] [--version] fileName
#####参数：
#####-n 或 --number 由 1 开始对所有输出的行数编号
#####-b 或 --number-nonblank 和 -n 相似，只不过对于空白行不编号
#####-s 或 --squeeze-blank 当遇到有连续两行以上的空白行，就代换为一行的空白行
#####-v 或 --show-nonprinting

###more(more命令会以一页一页的显示方便使用者逐页阅读，而最基本的指令就是按空白键（space）就往下一页显示，按 b 键就会往回（back）一页显示，而且还有搜寻字串的功能 。more命令从前向后读取文件，因此在启动时就加载整个文件)

##### more[-dlfpcsu] [-num] [+/pattern] [+linenum] [file ...]
- Enter    向下n行，需要定义。默认为1行  
- Ctrl+F   向下滚动一屏  
- 空格键   向下滚动一屏  
- Ctrl+B   返回上一屏  
- =        输出当前行的行号  
- ：f      输出文件名和当前行的行号  
- v        调用vi编辑器  
- !命令    调用Shell，并执行命令   
- q        退出more  



##linux上如何上传和下载文件
- yum install -y lrzsz
- 输入rz，从本地上传文件到linux
- 输入sz，从linux下载文件到本地


## 寻找文件夹
-find . -name "*.json"  
查找当前目录下所有带json后缀的文件
. 代表当前目录
-name 代表需要寻找的文件

##更改系统时间再改回来 
1、更改权限 su jenkins password:Dl7mdkzbMLwe0FBu  
2、切换root权限 sudo su - root  
3、date -s "2022-04-12 23:24:34"
4、yum install ntpdate 下载ntpdate服务 ntpdate  ntp.api.bz （上海时区）
5、重启对应docker服务，使得服务的时间可重新load


##清除缓存
 清理缓存  
echo 1 > /proc/sys/vm/drop_caches  
echo 2 > /proc/sys/vm/drop_caches  
echo 3 > /proc/sys/vm/drop_caches  




