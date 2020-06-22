def StorePoints(points, point_list, rc):
    if rc in [8,9,10,14,15,16,17,20,21,22,23,24,27,28,29,30,34,35,36]:
        for point in points:
            if point not in point_list:
                point_list.append(point)
    return point_list
