# 字符串和文本

代码块：

    x = "There are %d types of people." %10 // 数字 10 替代句中整型。
    binary = "binary" // binary 赋值给 binary
    do_not = "don't" // don't 赋值给 do_not
    y = "Those who know %s and those who %s." %(binary,do_not) // binary 和 do_not 替代句中字符串
    
    print x // 打印 x
    print y // 打印 y
    
    print "I said: %r." % x  // x 替代句中任意型 %r 用来调试比较好，因为它会现实变量的原始数据（raw data)
    print "I also said: '%s'." % y // y 替代句中字符串
    
    hilarious = False // False 赋值给 hilarious
    joke_evaluation = "Isn't that joke so funny?! %r" // 一段字符串赋值给 joke_evaluation
    
    print joke_evaluation % hilarious  // 打印
    w = "This is the left side of..." // 赋值 w
    e = "a string with a right side." // 赋值 e
    
    print w+e // 打印 w 连接 e
    
附加练习：

1. 通读这段程序，在每一行的上面写一行注释，给自己解释一下这一行的作用。

> done.
    
2. 找到所有“把一个字符串放进另一个字符串”的位置。总共有 4 个地方。

> line 8,13,14,19


3. 你确定只有 4 个位置吗？你怎么知道的？没准儿我骗你呢。

> 确定。 line 23不是，它是连接。

4.解释一下为什么 w 和 e 用 + 连接起来就可以生成一个更长的字符串。

> 连接。










# CHANGELOG

- 20181205
