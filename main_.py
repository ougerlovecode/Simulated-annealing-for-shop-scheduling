from datainput import myinput
from reset import reset
from piexchange import position_exchange
from timecalculate import time
import copy
# input
def S_A(p):
    # print("this is no.",i)

    # 随机重置p
    reset(p)
    best_p = copy.deepcopy(p)
    # 模拟退火算法
    class SA:
        def __init__(self, bestp = best_p, t0=3000, alpha=0.99, tf=0.0001):
            # self.time = time
            # self.iter = iter
            self.alpha = alpha
            self.T0 = t0
            self.Tf = tf
            self.T = t0
            self.best_p = bestp
            self.history = {'f': [], 'T': []}
        def run(self):
            flag = 0
            # 外循环迭代，当前温度小于终止温度的阈值
            while self.T > self.Tf: # and flag < 500
                # 得到的是新的时间和新的序列（或者还是原来的时间和序列）
                new_time, new_p = position_exchange(p, self.T)
                # 记录全局最优解
                if new_time < time(self.best_p):
                    self.best_p = copy.deepcopy(new_p)
                self.T *= self.alpha
                self.history['f'].append(new_time)
                self.history['T'].append(self.T)
                ###########
                if new_p == p:
                    flag += 1
                else:
                    flag = 0
            return new_time, new_p

    sa = SA()
    new_time, new_p = sa.run()

    # plt.plot(sa.history['T'], sa.history['f'])
    # plt.title('SA')
    # plt.xlabel('T')
    # plt.ylabel('time')
    # plt.gca().invert_xaxis()
    # plt.show()
    # return time(best_p), sa.best_p
    return new_time, new_p, sa.history
    # best_time = time(best_p)
    # if best_time < new_time:
    #     return best_time , best_p
    # else:
    #     return new_time, n


    # print(now_time)
    # for i in p:
    #     print(i[-1], end=",")
    # print("\n")
    # return now_time, p