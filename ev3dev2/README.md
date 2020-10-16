ev3dev（https://www.ev3dev.org）是一个可运行在Lego MINDSTORMS EV3控制器上的linux发行版本，它允许各种编程语言通过读写文件的方式对EV3进行编程。python可以调用ev3dev2库实现各种传感器数据的读取、中型/大型马达、声音和液晶显示屏的控制。
从零开始使用ev3dev2对乐高EV3机器人编程的步骤：https://www.ev3dev.org/docs/getting-started/
ev3dev2库文件 https://github.com/ev3dev/ev3dev-lang-python

程序写完后需要连接EV3将程序下载进去，这里我选择 visual studio code 编译环境
为方便后续使用我查看了ev3dev2库的源码并根据自己的理解写了接口说明，在查资料的过程中又发现了官方的接口说明，将结合二者的汉化版接口说明以及对于的示例代码放在这里供参考，希望能有所帮助
