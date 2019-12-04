import cv2
import numpy as np

img = cv2.imread('gabe.jpg')
# ne = img[0:50, 0:50]
# cv2.circle(img, (100, 100), 55, (250, 0, 0))
# cv2.imshow("image", ne)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


class Cell(object):

    """A cell is a block of the image with some upper bound on the size"""

    def __init__(self, start_x, start_y, width, height, pixels):
        """Can create a rectangular area of of wxh that contains
        the pixels specified.

        :start_x, start_y: the starting (top left corner of the rectangle)

        """
        self.start_x = start_x
        self.start_y = start_y
        self.width = width
        self.height = height
        self.pixels = pixels
        self.children = []


class QuadTree(Object):

    """QuadTree -- similar to binary tree but with four children"""

    def __init__(self, size_limit, image):
        """ Generates a quad decomposition of cells

        :size_limit: the min size of a cell to recurse to
        :image: image from opencv
        """
        self.size_limit = size_limit
        self.image = image
        self.root = Cell(0, 0, size_limit, size_limit, image)

    def split_tree(self):
        """ Recursively splits the image into rectangles """
        
        def subset(start_x, start_y, width, height, points):
            """ Returns the subset of points contained with the params """
            pass

        def split(cell, min_limit):
            if len(cell.points) <= min_limit:
                return cell

            width = cell.width / 2
            height = cell.height /2


