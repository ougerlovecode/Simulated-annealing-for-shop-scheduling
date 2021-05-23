def time(p):
    # 对特定序列下加工总时间的计算
    Wcount = len(p)
    Mcount = len(p[1])-1
    rtime = []
    for i in range(Wcount):
        rtime.append([])
    for i in range(Wcount):  # p[i][j] 工件i在机器j上的加工时间
        for j in range(Mcount):
            if i == 0:
                if j != 0:
                    rtime[0].append(p[0][j]+rtime[0][j-1])
                else:
                    rtime[0].append(p[0][j])
            else:
                if j == 0:
                    rtime[i].append(rtime[i-1][0] + p[i][0])
                else:
                    t_time = max(rtime[i-1][j],rtime[i][j-1])
                    rtime[i].append(t_time+p[i][j])
    return rtime[-1][-1]