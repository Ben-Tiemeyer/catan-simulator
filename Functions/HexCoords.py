def HexCoords(size, center):
    D = size
    alpha = D / 4
    B = round((3**(1/2))*alpha, 3)
    x1 = round(center[0], 3)
    y1 = round(center[1] + (2*alpha), 3)
    x2 = round(center[0] + B, 3)
    y2 = round(center[1] + alpha, 3)
    x3 = round(center[0] + B, 3)
    y3 = round(center[1]  - alpha, 3)
    x4 = round(center[0], 3)
    y4 = round(center[1] - (2*alpha), 3)
    x5 = round(center[0] - B, 3)
    y5 = round(center[1] - alpha, 3)
    x6 = round(center[0] - B, 3)
    y6 = round(center[1] + alpha, 3)
    return ([(x1,y1), (x2,y2), (x3,y3), (x4,y4), (x5,y5), (x6,y6)], B, center)
