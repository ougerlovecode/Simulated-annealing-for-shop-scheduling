def myinput():
    f = open( 'E:\\BIT\\optimization\\10-problem.txt', 'r' )
    t = 0
    n, m = 0, 0
    P=[]
    p = []
    # 对每一行进行处理，将加工时间存为p数列
    for line in f:
        line_p = []
        if '+' in line:
            t = 0
            if p:
                # print(p)
                t_p = p.copy()
                p.clear()
                if not t_p == []:
                    P.append(t_p)
        t += 1
        if t == 3:
            line=line.split()
            n,m= line[0], line[1]
            # print(n,m)
        if t >= 4:
            line = line.split()
            line_p = line[1::2]
            # print(line_p)
            p.append(line_p)
            # print(p)
    for i in range(len(P)):
        for j in range(len(P[i])):
            for k in range(len(P[i][j])):
                P[i][j][k] = int (P[i][j][k])
    for i in range(len(P)):
        for j in range(len(P[i])):
            P[i][j].append(j)
    return P