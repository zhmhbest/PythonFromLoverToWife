# PythonFromLoverToWife

- [Hello](demo-base.py)
- [字符串处理](demo-string.py)
- [字符串逆序](demo-str_reverse.py)
- [异常处理](demo-exception.py)
- [时间处理](demo-time.py)
- [彩色字体](demo-colorful_print.py)
- [匿名函数](demo-anonymous.py)
- [静态方法](demo-static.py)
- [可变参数](demo-args.py)
- [位运算](demo-bit.py)
- [深浅拷贝](demo-copy.py)
- [闭包](demo-closer.py)
- [装饰器](demo-decorate.py)
- [运算符重载](demo-operation_overload.py)
- [偏函数](demo-partial.py)
- [正则表达式](demo-regularization.py)
- [序列](demo-sequence.py)
- [多线程](demo-thread.py)
- [通用爬虫](demo-requests.py)
- [XPATH](demo-xpath.py)
- [Clipboard](demo-clipboard.py)
- [ReadPdf](demo-read_pdf.py)
- [MatrixCalculate](demo-matrix_calculate.py)

## 配置虚拟环境

### pip

#### 镜像

```bash
# Tsinghua
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
pip config set install.trusted-host pypi.tuna.tsinghua.edu.cn

# Aliyun
pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/
pip config set install.trusted-host mirrors.aliyun.com
```

#### 安装

```batch
REM Windows
pip install virtualenv
pip install virtualenvwrapper-win
```

```bash
# Linux
pip install virtualenv
pip install virtualenvwrapper
```

#### 使用

```bash
# 环境命令
activate
deactivate

# 系统命令
# virtualenv envname
# mkvirtualenv -p python3.6.8 envname
workon envname
lsvirtualenv
cdvirtualenv envname
rmvirtualenv envname

# 创建项目环境
# SET WORKON_HOME=%CD%
export WORKON_HOME=$(pwd)
mkvirtualenv venv
```

### conda

#### 镜像

```bash
# notepad %UserProfile%\.condarc
# vim ~/.condarc
conda config --set channel_alias "http://mirrors.tuna.tsinghua.edu.cn/anaconda"
conda config --add channels defaults
conda config --add default_channels "http://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2/"
conda config --add default_channels "http://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/pro/"
conda config --add default_channels "http://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r/"
conda config --add default_channels "http://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/"
conda config --add default_channels "http://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/"
conda config --set ssl_verify no
conda config --set show_channel_urls yes
conda clean -i
```

#### 使用

```bash
# 选择默认Shell
# conda init cmd.exe
# conda init bash

# 创建环境
# conda create -n python36 python=3.6.8
conda create -n <envname> python=<PYTHON_VERSION>

# 查看已创建的环境
conda env list

# 进入环境
conda activate <envname>

# 当前环境已安装的包
conda list

# 退出环境
conda deactivate

# 增删改
conda install -n <envname> <package>==<version>
conda remove -n <envname> <package>
conda update -n <envname> <package>

# 复制环境
# conda create -n test --clone python36
conda create -n <envname> --clone <EXISTED_ENV>

# 删除环境
conda remove -n <envname> --all
```

## 安装依赖

```bash
# 生成requirements（全部依赖）
pip freeze>requirements.txt

# 生成requirements（使用的主要依赖）
# pip install pipreqs
pipreqs . --encoding=utf8 --force

# 在线安装依赖
pip install -r requirements.txt [-i <SimpleURL>] [-f <HTML文件/本地目录>]

# 下载依赖
pip download -r requirements.txt -d packages

# 离线安装依赖
pip install -r requirements.txt --no-index -f packages
```
