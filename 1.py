
def lk(img, min, max):
    edges = cv.Canny(img,min, max)
    return edges

def detect(readimg):
    gray = cv.cvtColor(readimg, cv.COLOR_BGR2GRAY)
    gray = cv.bilateralFilter(gray, 0, 0, 0)
    gaussian = cv.GaussianBlur(gray, (5, 5), 0)
    edges = lk(gaussian, 80, 150)
    #修改合适的Hough变换参数以检测
    circles1 = cv.HoughCircles(edges, cv.HOUGH_GRADIENT, 1, 1000, param1=80, param2=10, minRadius=10, maxRadius=100)

    circles = circles1[0, :, :]
    circles = np.uint16(np.around(circles))
    for i in circles[:]:
        cv.circle(readimg, (i[0], i[1]), i[2], (0, 0, 255), 2)
        cv.circle(readimg, (i[0], i[1]), 2, (255, 0, 255), 1)
    ball_r = i[2]
    ball_x = i[0]
    ball_y = i[1]
    r, x, y = ball_r, ball_x, ball_y
    return r, x, y