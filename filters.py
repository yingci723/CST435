import numpy as np
from PIL import Image

def grayscale(img):
    img = np.array(img)
    gray = 0.299*img[:,:,0] + 0.587*img[:,:,1] + 0.114*img[:,:,2]
    return Image.fromarray(gray.astype(np.uint8))

def gaussian_blur(img):
    kernel = np.array([[1,2,1],[2,4,2],[1,2,1]]) / 16
    img = np.array(img)
    padded = np.pad(img, 1, mode='edge')
    output = np.zeros_like(img)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            output[i,j] = np.sum(kernel * padded[i:i+3, j:j+3])
    return Image.fromarray(output.astype(np.uint8))

def sobel_edge(img):
    img = np.array(img)
    gx = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
    gy = np.array([[1,2,1],[0,0,0],[-1,-2,-1]])
    padded = np.pad(img, 1, mode='edge')
    edge = np.zeros_like(img)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            sx = np.sum(gx * padded[i:i+3, j:j+3])
            sy = np.sum(gy * padded[i:i+3, j:j+3])
            edge[i,j] = min(255, abs(sx) + abs(sy))
    return Image.fromarray(edge.astype(np.uint8))

def sharpen(img):
    kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
    img = np.array(img)
    padded = np.pad(img, 1, mode='edge')
    output = np.zeros_like(img)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            val = np.sum(kernel * padded[i:i+3, j:j+3])
            output[i,j] = np.clip(val, 0, 255)
    return Image.fromarray(output.astype(np.uint8))

def brightness(img, value=30):
    img = np.array(img)
    img = np.clip(img + value, 0, 255)
    return Image.fromarray(img.astype(np.uint8))
