# python3
> create by nohi 20210628

* 参考：瘳雪峰博客[https://www.liaoxuefeng.com/wiki/1016959663602400/1018491156860224]
* 第一版：git: https://github.com/nohi-python/py3-webapp.git
    * 该版本为按博客写的第一版，照搬、照抄
* 当前版本，为第二版，
    * 增加说明、模块分类
    * 基础版本

## 模块
```
├── config
│   ├──config_default.py                    # 默认配置文件
│   └── config_override.py                  # 配置文件，优先级高于default
├── dist                                    # 打包后目录
├── script                                  # 数据库初始化脚本
├── test                                    # 测试目录
├── www                                     # 应用主目录
│   ├── static                              # 静态文件
│   ├── common                              # 公用模块
│   │   ├── config                          # 配置文件解析代码
│   │   ├── db                              # 数据库解析
│   │   └── web                             # http解析
│   ├── model                               # 模型层
│   ├── templates                           # 视图模板
│   ├── app.py                              # 程序入口函数
│   └── handlers.py                         # api注册
├── .gitignore                              # Git忽略文件
└──  README.md                              # 说明文档
```

### 各种小功能
* watchdog：文件监控
  *  启动命令： ./www/pymonitor.py app.py
  * 为解决模块引用问题： 
    ```
    子目录引用需要使用 sys.path.append("..") 或 sys.path.append("../..")因目录层级不同而不同 
    ```
    