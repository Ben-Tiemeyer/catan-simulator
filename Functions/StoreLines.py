def StoreLines(points, line_list, rc):
    if rc in [8,9,10,14,15,16,17,20,21,22,23,24,27,28,29,30,34,35,36]:
        for number in [(0,1), (1,2), (2,3), (3,4), (4,5), (5,0)]:
            if sorted((points[number[0]], points[number[1]])) not in line_list:
                line_list.append(sorted((points[number[0]], points[number[1]])))
    return line_list
