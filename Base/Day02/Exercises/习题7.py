# 练习三元运算符的使用。模拟用户的消费付款，需求：
#     * 让用户输入银行卡的余额
#     * 让用户输入要付款的金额
#     * 使用三元运算符判断银行卡余额是否足够付款，并将结果赋值给一个变量
#     * 如果足够则'使用银行卡付款'，否则为'余额不足'
#     * 打印变量


surplus = int(input('请输入你的余额：'))
money = int(input('请输入付款金额：'))
enough = '使用银行卡付款'
if surplus > money:
    print(enough)
else:
    '余额不足'
