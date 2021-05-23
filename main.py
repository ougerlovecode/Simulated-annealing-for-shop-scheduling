from main_ import S_A
from datainput import myinput
import matplotlib.pyplot as plt

my_P = myinput()
for i in range(5):
    print("this is no.", i)

    p = my_P[i]
    now_time = float('inf')
    better_p = p
    for j in range(1):
        # 此处是对十一个例子进行遍历
        new_time, new_p, d_history = S_A(p)
        # 此处是我做的一个优化，对同一个例子运行多次，选择最好的那个结果，有点效果
        if new_time < now_time:
            now_time = new_time
            better_p = p
        else:
            # 啥也不干
            better_p = better_p
    # 绘制图像
    plt.plot(d_history['T'], d_history['f'])
    plt.title('SA')
    plt.xlabel('T')
    plt.ylabel('time')
    plt.gca().invert_xaxis()
    plt.show()
    ##########
    filename = open('C:\\Users\\14004\\Desktop\\mylearning.txt', 'a+')
    print(now_time, file=filename)
    for i1 in better_p:
        print(i1[-1], end=",", file=filename)
    print("\n", file=filename)
    filename.close()

