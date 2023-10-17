# PySideUI

customized ui components for Qt python bindings


### 安装

> pip install PySideUI

或升级

> pip install PySideUI --upgrade -i https://pypi.tuna.tsinghua.edu.cn/simple


### 使用
#### Button
```
btn = PrimaryBtn('测试', {'color': 'red', 'background-color': 'pink'}, clicked=lambda:print('hello world'))
# 通过字典设置样式，点击事件赋值给 clicked 参数

btn.clickedFunc = lambda: print('hahah')
```

