# 项目描述

chromium 浏览器的文件镜像。

注：此 pypi 包非 chromium 发行，但内含从 chromium 官网下载的浏览器文件。

此包的版本号将与所包含的 chromium 浏览器的版本号保持一致。例如：存放 '100.2.3' 版本的 chromium 的 chromiumfile 包的版本号也将为 '100.2.3' 。

# 作者信息

昵称：lcctoor.com

域名：lcctoor.com

邮箱：lcctoor@outlook.com

[主页](https://lcctoor.github.io/arts/) \| [微信](https://lcctoor.github.io/arts/arts/static/static-files/WeChatQRC.jpg) \| [Python交流群](https://lcctoor.github.io/arts/arts/static/static-files/PythonWeChatGroupQRC.jpg) \| [捐赠](https://lcctoor.github.io/arts/arts/static/static-files/DonationQRC-1rmb.jpg)

# Bug提交、功能提议

您可以通过 [Github-Issues](https://github.com/lcctoor/arts/issues)、[微信](https://lcctoor.github.io/arts/arts/static/static-files/WeChatQRC.jpg) 与我联系。

# 安装

```
pip install chromiumfile
```

# 教程

```python
from chromiumfile import (
    chromium_dir,  # chromium 文件夹路径
    bootstrap_file  # 浏览器启动文件路径, 即 chrome.exe 的路径
)
```
