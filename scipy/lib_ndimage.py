import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage


# morphology
def morhpo():
    np.random.seed(0)
    x = np.zeros((32, 32))
    x[10:-10, 10:-10] = 1
    x[np.random.randint(0, 32, 30), np.random.randint(0, 32, 30)] = 1

    open_x = ndimage.binary_opening(x)  # suppression des artefactes
    plt.imshow(open_x)

    plt.show()


def managing_img():
    print('processing...')

    image = plt.imread('img.jpg')  # reading image
    image = image[:, :, 0]  # making image on 2d
    print('shape:', image.shape)

    # for distinguish well the color with histogram
    # image_2 = np.copy(image)
    # plt.hist(np.ravel(image_2), bins=255 )

    image = image > 150
    open_x = ndimage.binary_opening(image)  # suppression des artefactes

    # for putting etiquette's
    # label_image, nb_labels = ndimage.label(open_x)
    # plt.imshow(label_image)

    plt.imshow(open_x)
    plt.show()
    print('terminated')


managing_img()
