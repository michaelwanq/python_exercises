# 练习 5-6：人生的不同阶段 设置变量 age 的值，再编写一个 if-elif-else 结构，
# 根据 age 的值判断一个人处于人生的哪个阶段。
#  如果年龄小于 2 岁，就打印一条消息，指出这个人是婴儿。
#  如果年龄为 2（含）～4 岁，就打印一条消息，指出这个人是幼儿。
#  如果年龄为 4（含）～13 岁，就打印一条消息，指出这个人是儿童。
#  如果年龄为 13（含）～20 岁，就打印一条消息，指出这个人是青少年。
#  如果年龄为 20（含）～65 岁，就打印一条消息，指出这个人是成年人。
#  如果年龄超过 65 岁（含），就打印一条消息，指出这个人是老年人。
# age = 1
# age = 3
# age = 7
age = 16
# age = 30
# age = 70
if age < 2:
    print("你输入的年龄是%s岁，你是一名婴儿" %age)
elif age < 4:
    print("你输入的年龄是%s岁，你是一名幼儿" %age)
elif age < 13:
    print("你输入的年龄是%s岁，你是一名儿童" %age)
elif age < 20:
    print("你输入的年龄是%s岁，你是一名青少年" %age)
elif age < 65:
    print("你输入的年龄是%s岁，你是一名成年人" %age)
else:
    print("你输入的年龄是%s岁，你是一名老年人" %age)