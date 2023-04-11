# anylink-openwrt
在openwrt上运行anylink

在openwrt21.02上测试成功，其他版本未测试<br />
因为我这里是x86的，arm暂未测试<br />
其他版本，其他架构可以提交issues打包<br />

# 运行方法
下载到/usr/share/AnyLink/下<br />
看起来应该是这样<br />
```
root@OpenWrt:~# tree /usr/share/AnyLink/
/usr/share/AnyLink/
├── LICENSE
├── anylink
├── conf
│   ├── anylink.db
│   ├── files
│   │   ├── index.html
│   │   └── info.txt
│   ├── profile.xml
│   ├── server-sample.toml
│   ├── server.toml
│   ├── vpn_cert.crt
│   └── vpn_cert.key
└── systemd
    └── anylink.service

3 directories, 11 files
```
service中文件直接导入到/etc/init.d/下<br />
加执行权限
```
chmod +x /etc/init.d/AnyLink
```
启动
```
/etc/init.d/AnyLink start
```
