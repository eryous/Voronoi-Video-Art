from quad_sampler import Quad, __average_rgb__
import numpy as np
import cv2
import matplotlib.pyplot as plt
from scipy.spatial import Delaunay
import math
import os

def circumcircle(x1, y1, x2, y2, x3, y3):
    a2 = x1 - x2
    a3 = x1 - x3
    b2 = y1 - y2
    b3 = y1 - y3
    d1 = x1 * x1 + y1 * y1
    d2 = d1 - x2 * x2 - y2 * y2
    d3 = d1 - x3 * x3 - y3 * y3
    ab = (a3 * b2 - a2 * b3) * 2
    xa = (b2 * d3 - b3 * d2) / ab - x1
    ya = (a3 * d2 - a2 * d3) / ab - y1
    x = x1 + xa
    y = y1 + ya
    r = math.sqrt(xa * xa + ya * ya)
    return x, y, r

def voro(packed_input):
    image, index, dir, error = packed_input
    print("This is the image path: ",image)
    img = cv2.imread(image)
    q = Quad(img, error_rate=error, is_root=True)

    xs, ys = q.generate_seeds()
    for leaf in q.leaves_copy:
        cv2.rectangle(img,(leaf.y, leaf.x), (leaf.y+leaf.height, leaf.x+leaf.width),__average_rgb__(leaf.img), cv2.FILLED)

    points = np.array(list(zip(xs, ys)))


    tri = Delaunay(points)
    coords = points[tri.simplices]
    circle_cord=[]
    radii = []
    circle_tri = {}
    for i in range(0, len(points[tri.simplices])):
        x, y, r = circumcircle(coords[i][0][0], coords[i][0][1],
                            coords[i][1][0], coords[i][1][1],
                            coords[i][2][0], coords[i][2][1])
        circle_cord.append((x,y))
        circle_tri[i] = (int(x),int(y))
        radii.append(r)

    # print(x_mids)
    # print(y_mids)
    # print(radii)

    # for i in range(min(len(x_mids), len(y_mids))):
        # cv2.circle(img, (int(x_mids[i]), int(y_mids[i])),
                # int(radii[i]), (250, 0, 0))


    for i in range(len(tri.simplices)):
        current = circle_tri[i]
        neighbors = tri.neighbors[i]
        temp = []
        for n in neighbors:
            if n >= 0:
                temp.append(n)


        for n in temp:
            center = circle_tri[n]
            cv2.line(img,center,current,(0,0,0))


    # plt.triplot(points[:, 0], points[:, 1], tri.simplices.copy())
    # plt.plot(points[:, 0], points[:, 1], 'o')
    # # plt.show()
    os.chdir(dir)
    cv2.imwrite(index+'.jpg', img)
    os.chdir("../..")
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
