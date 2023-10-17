# pygmlib

[GMLib](https://github.com/oldprincess/gmlib)项目的python绑定，利用pybind11进行绑定

已经通过测试的环境

|操作系统|CPU|python版本|
|:-:|:-:|:-:|
|Windows11|i5-12500H|3.9|
|Windows11|i5-12500H|3.10|

## 1 快速开始

### 1.1 通过pypi安装（推荐）

```python
pip install pygmlib
```

### 1.2 通过源码包安装（推荐）

在pypi主页下载pygmlib项目的源码包并解压

* 运行

```
pip install ./pygmlib
```

### 1.3 通过github项目安装

* 克隆仓库

```
git clone https://github.com/oldprincess/py-gmlib.git
```

* 获取子模块

```
cd py-gmlib
git submodule update --init --recursive
cd ..
```

* pip安装pygmlib

```
pip install ./pygmlib
```

## 2 支持的密码算法

* SM3
* SM4: ECB, CBC, CFB, OFB, CTR, GCM
* AES: ECB, CBC, CFB, OFB, CTR, GCM


## 3 使用样例

下面的样例实现SM4算法ECB模式的加密和解密功能，并校验正确性

```python
import pygmlib

sm4_key = bytes(16)  # 16 bytes ZERO
sm4_pt = bytes(16)  # 16 bytes ZERO
# sm4 ecb encrypt
sm4e = pygmlib.cipher.Sm4EcbEncryptor(sm4_key)
ct = sm4e.update(sm4_pt)
ct += sm4e.final()
# sm4 ecb decrypt
sm4d = pygmlib.cipher.Sm4EcbDecryptor(sm4_key)
pt = sm4d.update(ct)
pt += sm4d.final()

assert pt == sm4_pt
# key: 00000000000000000000000000000000
# pt : 00000000000000000000000000000000
# ct : 9f1f7bff6f5511384d9430531e538fd3
print("key:", sm4_key.hex())
print("pt :", sm4_pt.hex())
print("ct :", ct.hex())
```
