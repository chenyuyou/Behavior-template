# Behavior-template

积累一些行为实验的代码，方便以后进一步作更多实验。

## 注意事项：
1. 如果局域网部署，用otree devserver 局域网实际地址:端口  替换otree devserver localhost:端口。
2. 要关闭实验中debug info，请在setting.py中将
```python
if environ.get ('OTREE_PRODUCTION') not in {None, '', '0'}:
    DEBUG = False
else:
    DEBUG = True
```
改为
```python
if environ.get ('OTREE_PRODUCTION') not in {None, '', '0'}:
    DEBUG = True
else:
    DEBUG = False
```
