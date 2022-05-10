
#### 设置变量@
```
set @name = '场景命中节点全部遗漏' or '遗漏1-1' or '遗漏2-1';  
-- SELECT DISTINCT word from see_management_4.keyword_detail where keyword_lib_id  in ( SELECT id from see_management_4.keyword_lib WHERE name = @name order by id ASC) order by word ASC  ;   
SELECT DISTINCT rule_condition->'$.conditions' FROM see_management_4.business_scene bs  WHERE name = @name  

```

#### sql注入
```
SQL注入即是指web应用程序对用户输入数据的合法性没有判断或过滤不严，攻击者可以在web应用程序中事先定义好的查询语句的结尾上添加额外的SQL语句，
在管理员不知情的情况下实现非法操作，以此来实现欺骗数据库服务器执行非授权的任意查询，从而进一步得到相应的数据信息。
```


