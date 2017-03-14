# 读取excel铁路数据并重新整合

## 环境依赖
- python3
- xlrd
- xlwt
- xlutils

```
pip install xlrd xlwt xlutils
```

## 目录文件
 - data 数据目录
 - logs 运行日志和错误日志
 - plf.py 整合车次客座率信息脚本
 - station.py 整合车次站点信息脚本

## 脚本运行

将数据文件放到 data 目录下，或者修改 plf.py station.py 的 data_dir 变量指定具体目录；save_dir 变量指定保存的 excel 文件名

- 站点信息整合
```
python station.py
```

- 客座率信息整合
```
python plf.py
```

Thanks
------
Create by phachon@163.com