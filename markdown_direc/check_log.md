```
docker 

su ops

java -jar /opt/arthas/ar**-boot

logger

logger -c {classLoaderHash}1d56ce6a --name {name2}com.zhuiyi.see --level debug


```
##### 根据时间找日志对应error并打印十行
```

grep "2021-06-10 19:\[0-5][0-9]" 日志名 | grep "ERROR" -B10

grep - E "2021-06-10 19:\[0-5][0-9]|2021-06-10 20:\[0-5][0-9] "  日志名 
```