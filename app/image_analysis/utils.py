import numpy as np
import cv2


def create_mask(image, tminColor, tdifColor):
    minc = np.min(image, axis=2)
    maxc = np.max(image, axis=2)
    tdif = maxc - minc
    Ipc = image[:,:,0]
    mask = np.logical_or(Ipc < tminColor, tdif > tdifColor)
    return mask

