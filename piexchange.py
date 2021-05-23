# 这里的random不知道是不是真的随机，还是伪随机，如果是伪随机可能会对结果产生一点影响，这样的话之后需要改进
import random
import math
import copy
from timecalculate import time
def position_exchange(p,T):
    now_time = time(p)
    # best_p = copy.deepcopy(p)
    Wcount = len(p)
    # Mcount = len(p[1])-1
    x = random.randrange(0, Wcount-1, 1)
    y = random.randrange(0, Wcount-1, 1)
    p[x], p[y] = p[y], p[x]
    new_time = time(p)
    #做出了改变，选择了新位置
    if new_time < now_time:
        return new_time, p
    elif random.random() < math.exp((now_time-new_time)/T):
        return new_time, p
    #没有改变，仍在原来的位置
    else:
        #把序列换回来
        p[x], p[y] = p[y], p[x]
        #返回序列
        return now_time, p