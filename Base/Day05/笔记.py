# 练习题是为了练习操作而不是为了项目思维
'>>>>>>>>>概览>>>>>>>>概览>>>>>>>>概览'''
# 字典增删改查
# 字典遍历

# 定义调用
# 传参 形参、实参
# 返回值

'需求'
# 一个变多个要考虑会不会变更多
# 列表适合保存同种类型的数据
# for的else必定和break配合使用

'字典的注意点'
# 字典数据无序，只可键值存取，不可下标切片
# 字典没有重复键
# 字典的查找不存在的值get不报错，且找不到可返回一个设定的值，如‘找不到’
# 且因get为查找操作，设置的默认值并不添加

'字典的遍历'
# 直接遍历字典的结果 = 遍历字典的keys
# keys 得到一个列表，里面全是键
# values 得到一个列表，里面全是值
# items 得到一个列表，里面是多个元组，元组里是键值

'常用的字典的高级遍历'
# info = {}
# for k,v in info.items():

'enumerate()函数'
# 列表高级遍历 既有下标又有数据
# info = []
# for i,data in enumerate(info):

'内置函数的基本使用'
# len max min del
# cmp >> Python2

'函数注意点和帮助信息'
# 函数执行结束之后，会回到调用函数的地方
# return 函数就结束

'帮助信息定义方式'
# 函数的帮助信息 摁C键放函数上 快捷键C+Q
# def func():
#     '帮助信息'

'None'
# 没有return，则返回值默认为None
# 暂时不给变量赋值 则可以赋值为None
