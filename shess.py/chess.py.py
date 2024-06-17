import numpy as np
import matplotlib.pyplot as plt
# numpy baray mohasebat adadi
# matplotlib baray rasm nemodar va tasvir


def fill(s, n, img):
    a = 32*s
    b = 32*(s+1)
    c = 32*n
    d = 32 * (n+1)
    for x in range(a, b):
        for y in range(c, d):
            img[x, y] = 255


img = np.zeros([256, 256])
for s in range(8):
    for n in range(8):
        if (s+n) % 2 == 0:
            fill(s, n, img)

plt.imshow(img, cmap='gray')
plt.show()
