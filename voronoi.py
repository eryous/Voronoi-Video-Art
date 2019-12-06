import cv2
import numpy as np
import queue

# ne = img[0:50, 0:50]
# cv2.circle(img, (100, 100), 55, (250, 0, 0))
# cv2.imshow("image", ne)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


class Cell(object):

    """A cell is a block of the image with some upper bound on the size"""

    def __init__(self, start_x, start_y, width, height, image):
        """Can create a rectangular area of of wxh that contains
        the pixels specified.

        :start_x, start_y: the starting (top left corner of the rectangle)

        """
        self.start_x = start_x
        self.start_y = start_y
        self.width = width
        self.height = height
        self.children = []
        self.img = image


class QuadTree:

    """QuadTree -- similar to binary tree but with four children"""

    def __init__(self, size_limit,  cell, error_rate=0.5, is_root=False):
        """ Generates a quad decomposition of cells

        :size_limit: the min size of a cell to recurse to
        :image: image from opencv
        """
        self.size_limit = size_limit
        self.cell = cell
        self.error_rate = error_rate
        self.is_root = is_root
        self.is_leaf = self.is_leaf()
        self.leaves = []
        if is_root:
            self.leaves = self.generate()

    def generate(self):

        width = self.cell.width / 2
        height = self.cell.height / 2

        leaves = []
        qu = queue.Queue()
        qu.put(self)

        while qu.empty() is False:
            q_size = qu.qsize()
            for _ in range(q_size):
                child = qu.get()
                if child.is_leaf is False:
                    tl, tr, bl, br = child.split()
                    qu.put(tl)
                    qu.put(tr)
                    qu.put(bl)
                    qu.put(br)
                else:
                    leaves.append(child)

        return leaves

    def is_leaf(self):
        """Check whether this node is a leaf """
        return self.cell.height * self.cell.width <= self.size_limit or __error__(self.cell.img) <= self.error_rate

    def split(self):
        """
         Recursively splits the image into rectangles

        :returns: the split 4 chidren
        """
        child_width = math.ceil(self.cell.width / 2)
        child_height = math.ceil(self.cell.height / 2)
        top_left = Quad(size_limit, Cell(self.cell.start_x, self.cell.start_y, child_height, child_width, self.cell.img[:child_height, :child_width, :]))
        top_right=Quad(size_limit, Cell(self.cell.start_x, self.cell.start_y+child_width, child_height, child_width, self.cell.img[:child_height, :child_width, :]))

        bottom_left=top_right=Quad(size_limit, Cell(self.cell.start_x+child_height, self.cell.start_y, child_height, child_width, self.cell.img[:child_height, :child_width, :]))
        bottom_right=Quad(size_limit, Cell(self.cell.start_x+child_height, self.cell.start_y+child_width, child_height, child_width, self.cell.img[:child_height, :child_width, :]))
        self.children=[top_left, top_right, bottom_left, bottom_right]
        return top_left, top_right, bottom_left, bottom_right

    def generate_seeds(self):
        """Generate seeds """
        point_x=np.zeros(len(self.leaves))
        point_y=np.zeros(len(self.leaves))

        for i in range(len(self.leaves)):
            block=self.leaves.pop()
            x=block.cell.start_x
            y=block.cell.start_y
            w=block.cell.width
            h=block.cell.height
            point_y[i]=x + w / 2
            point_x[i]=y + h / 2

        return point_x, point_y


def __error__(img):
    """Compute the error """
    avg_rgb=__average_rgb__(img)
    d2=np.sum(np.power((img - avg_rgb) / 255, 2), axis=2)
    err=d2.max(axis=1).max(axis=0).max()
    return err

def __average_rgb__(img):
    """Get average rgb value """
    r=np.average(img[:, :, 0])
    g=np.average(img[:, :, 1])
    b=np.average(img[:, :, 2])
    return np.array([r, g, b])




img=cv2.imread('gabe.jpg')
quad = QuadTree(64, Cell(0, 0, img.shape[0], img.shape[1], img),is_root=True)
print(quad.leaves)
x,y = quad.generate_seeds()
print(x,y)

