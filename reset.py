#这里的random不知道是不是真的随机，还是伪随机，如果是伪随机可能会对结果产生一点影响，这样的话之后需要改进
import random
def reset(p):
    random.shuffle(p)
    return p