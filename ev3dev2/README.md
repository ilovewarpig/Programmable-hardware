ev3dev（https://www.ev3dev.org）是一个可运行在Lego MINDSTORMS EV3控制器上的linux发行版本，它允许各种编程语言通过读写文件的方式对EV3进行编程。python可以调用ev3dev2库实现各种传感器数据的读取、中型/大型马达、声音和液晶显示屏的控制。
从零开始使用ev3dev2对乐高EV3机器人编程的步骤：https://www.ev3dev.org/docs/getting-started/
ev3dev2库文件 https://github.com/ev3dev/ev3dev-lang-python

程序写完后需要连接EV3将程序下载进去，这里我选择 visual studio code 编译环境
为方便后续使用我查看了ev3dev2库的源码并根据自己的理解写了接口说明，在查资料的过程中又发现了官方的接口说明，将结合二者的汉化版接口说明以及对于的示例代码放在这里供参考，希望能有所帮助


环境配置：
1. 安装python https://www.python.org/downloads/windows/
2. 安装ev3dev2包 
    python -m  pip install --upgrade pip
    pip install python-ev3dev2
3. 安装visualstudio code https://code.visualstudio.com/
4. 安装python、ev3dev2拓展插件(extension) 详见 https://github.com/ev3dev/vscode-hello-python
5. 下载vscode-hello-python-master 详见 https://github.com/ev3dev/vscode-hello-python
6. 连接ev3， 识别后点击hello.py 按F5自动下载程序并运行
7. 新建py文件，编写程序。执行时需要修改配置文件中的文件路径（hello.py修改为你的py文件名）
