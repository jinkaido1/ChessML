import cv2
import os

"""
We will flip all training images vertically and rotate them 3x by 90 degrees.
Result will be 2 x 4 x #traindata 
"""


class Image:
    path = ""
    filename = ""
    extension = ""
    img = None

    def __init__(self, path, filename):
        self.path = path
        self.filename, self.extension = os.path.splitext(filename)
        self.img = cv2.imread(path + filename)

    def flip(self):
        print("Flipping Image", self.path, self.filename)
        flipped = cv2.flip(self.img, +1)
        cv2.imwrite(self.path + self.filename + "_flipped" + self.extension, flipped)

    def rotate(self):
        print("Rotating Image", self.path, self.filename)
        rot90 = cv2.rotate(self.img, cv2.ROTATE_90_CLOCKWISE)
        rot180 = cv2.rotate(self.img, cv2.ROTATE_180)
        rot270 = cv2.rotate(self.img, cv2.ROTATE_90_COUNTERCLOCKWISE)
        cv2.imwrite(self.path + self.filename + "_90" + self.extension, rot90)
        cv2.imwrite(self.path + self.filename + "_180" + self.extension, rot180)
        cv2.imwrite(self.path + self.filename + "_270" + self.extension, rot270)


def augment_images(path):
    for filename in os.listdir(path):
        if filename.lower().endswith(".jpg") or filename.lower().endswith(".jpeg"):
            img = Image(path, filename)
            img.flip()

    for filename in os.listdir(path):
        if filename.lower().endswith(".jpg") or filename.lower().endswith(".jpeg"):
            img = Image(path, filename)
            img.rotate()


if __name__ == "__main__":
    augment_images("data/validation_aug/empty/")
    augment_images("data/validation_aug/bb/")
    augment_images("data/validation_aug/bk/")
    augment_images("data/validation_aug/bn/")
    augment_images("data/validation_aug/bp/")
    augment_images("data/validation_aug/bq/")
    augment_images("data/validation_aug/br/")
    augment_images("data/validation_aug/wb/")
    augment_images("data/validation_aug/wk/")
    augment_images("data/validation_aug/wn/")
    augment_images("data/validation_aug/wp/")
    augment_images("data/validation_aug/wq/")
    augment_images("data/validation_aug/wr/")