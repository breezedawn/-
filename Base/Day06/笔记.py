' 全局变量和局布变量 '''
' return多个返回值>>>>自动打包 '
' 打包和拆包 '
'缺省参数和关键字参数'
'不定长参数*和**'
'引用>>>>>内存起始地址>>>>>>>可变类型和不可变类型'
' += 和 =+ '

# 如果用全局变量global前最好加 g_ 看起来清晰

# 垃圾回收；函数局部变量函数使用完毕就被回收
# 全局变量一直存在，占内存

# 全局变量适用于不同场景
# 1.global
# 2.return 返回值传参
# 3.函数嵌套

# 快速创建函数 在调用不存在的函数上摁ALT + 回车

# 函数返回多个值

# 打包 >>>自动打包
# 解包
# 元组的打包拆包经常用

# 缺省参数 必须写在参数列表最后
# 关键字参数 命名参数
# 不定长参数/可变长参数 * 会用元组打包，** 会用字典打包 数据可任意多或为空
# 缺省和不定长混用 缺省必须写在不定长后面，最好不用
# 没人要的位置参数用*args，没人要的关键字参数用**kwargs
# 传实参时的多个参数可用一个变量打包，传进去不想以包的形式就在实参时加*或**拆包

# 快速交换变量值  a,b = b,a

#引用
# 变量通过内存起始地址位置来查找数据
# 可变类型和不可变类型
# 可变类型 修改数据内容，数据的内存起始地址不变 如 列表，字典
# 不可变类型 一旦数据发生变更，内存地址必定发生变化 如 数字，布尔，字符串，元组

# += 会把数据添加到原列表后面
# =+ 会生成一个新的列表
