from quad_sampler import Quad
import numpy as np
import cv2
import matplotlib.pyplot as plt
from scipy.spatial import Delaunay

img = cv2.imread('flower.jpg')
q = Quad(img, error_rate=0.3, is_root=True)

xs, ys = q.generate_seeds()
points = np.array(list(zip(xs,ys)))
# for i in range(min(len(xs), len(ys))):
    # cv2.circle(img, (int(xs[i]), int(ys[i])), 2, (250, 0, 0))

tri = Delaunay(points)
print(tri.simplices[0])
plt.triplot(points[:,0], points[:,1], tri.simplices.copy())
plt.plot(points[:,0], points[:,1], 'o')
plt.show()



# cv2.imshow("image", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


