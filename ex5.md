
代码块（更多的变量和打印）：


    my_name = "Zed A. Shaw"
    my_age = 35 # not a line
    my_height = 74 # inches
    my_weight = 180 #lbs
    my_eyes = "Blue"
    my_teeth = "white"
    my_hair = "Brown"
    cm = my_height / 0.393700787
    kg = my_weight / 2.20462262

    print "Let's talk about %s." % my_name
    print "He's %d inches tall." % my_height
    print "He's %d pounds heavy." % my_weight
    print "Actually that's not too heavy."
    print "He's got %s eyes and %s hair." %(my_eyes,my_hair)
    print "His teeth are usually %s depending on the coffee." % my_teeth
    print "He's %d cms tall." % cm
    print "He's %d kgs heavy." % kg

    # this line is tricky, try to get it exactly right
    print "If I add %d,%d,and %d I get %d." %(my_age,my_height,my_weight,my_age + my_height + my_weight)


附加练习：

1.修改所有的变量名字，把它们前面的my_去掉。确认将每一个地方都改掉，不只是使用=赋值过的地方。

> done.

2.试着使用更多的格式化字符。例如，%r 就是非常有用的一个，它的含义是：“不管什么都打印出来。“

> done.

3.在网上搜索所有的 python 格式化字符。



|：格式化符号：|：说明：|
-----------------
|：%c：| 转换成字符（ASCII 码值，或者长度为一的字符串）|

|：%r：|优先用repr()函数进行字符串转换|

|：%s：|优先用str()函数进行字符串转换|

|%d / %i|转成有符号十进制数|

|%u|转成无符号十进制数|

|%o|转成无符号八进制数|

|%x / %X|转成无符号十六进制数（x / X 代表转换后的十六进制字符的大小写）|

|%e / %E|转成科学计数法（e / E控制输出e / E）|

|%f / %F|转成浮点数（小数部分自然截断）|

|%g / %G|%e和%f / %E和%F 的简写|

|%%|输出% （格式化字符串里面包括百分号，那么必须使用%%）|

4.试着使用变量将英寸和磅转换成厘米和千克。不要直接键入答案。使用 python 的数学计算功能来完成。

> done.




# CHANGELOG

- 20181204
