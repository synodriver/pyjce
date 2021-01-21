# pyjce2

[![pypi](https://img.shields.io/pypi/v/pyjce2.svg)](https://pypi.org/project/pyjce2/) 
![python](https://img.shields.io/pypi/pyversions/pyjce2)
![implementation](https://img.shields.io/pypi/implementation/pyjce2)
![wheel](https://img.shields.io/pypi/wheel/pyjce2)
![license](https://img.shields.io/github/license/synodriver/pyjce.svg)

- 参考了 [pyjce](https://github.com/washingtown/PyJce)
- 原版只是实现了反序列化,此版本加入了序列化功能

- v0.1.0 大改 使用pydantic验证类型 自动读写jce结构体
- v0.1.1 弃用python3.7支持,只支持py3.8+ 
  
    下一步: 完善单元测试

## 使用参考

- 命令行
```
python -m pyjce 1606e686a8e689b92100fa8618e4bda0e5b185e784b6e79c9fe79a84e8a7a3e5af86e4ba86
```