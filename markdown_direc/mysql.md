
#### ���ñ���@
```
set @name = '�������нڵ�ȫ����©' or '��©1-1' or '��©2-1';  
-- SELECT DISTINCT word from see_management_4.keyword_detail where keyword_lib_id  in ( SELECT id from see_management_4.keyword_lib WHERE name = @name order by id ASC) order by word ASC  ;   
SELECT DISTINCT rule_condition->'$.conditions' FROM see_management_4.business_scene bs  WHERE name = @name  

```

#### sqlע��
```
SQLע�뼴��ָwebӦ�ó�����û��������ݵĺϷ���û���жϻ���˲��ϣ������߿�����webӦ�ó��������ȶ���õĲ�ѯ���Ľ�β����Ӷ����SQL��䣬
�ڹ���Ա��֪��������ʵ�ַǷ��������Դ���ʵ����ƭ���ݿ������ִ�з���Ȩ�������ѯ���Ӷ���һ���õ���Ӧ��������Ϣ��
```


