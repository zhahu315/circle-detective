
def detect(readimg):
    gray = cv.cvtColor(readimg, cv.COLOR_BGR2GRAY)
    gray = cv.bilateralFilter(gray, 0, 0, 0)
    #sp = cv.bilateralFilter(gray, 0, 0, 0)
    gaussian = cv.GaussianBlur(gray, (9, 9), 2)
    #修改合适的Hough变换参数以检测
    circles1 = cv.HoughCircles(gaussian, cv.HOUGH_GRADIENT, 1, 1000, param1=80, param2=10, minRadius=5, maxRadius=100)

    circles = circles1[0, :, :]
    circles = np.uint16(np.around(circles))
    for i in circles[:]:
        cv.circle(readimg, (i[0], i[1]), i[2], (0, 0, 255), 2)
        cv.circle(readimg, (i[0], i[1]), 2, (255, 0, 255), 1)
    ball_r = i[2]
    ball_x = i[0]
    ball_y = i[1]
    #cv.imwrite('result.png', readimg)
    r, x, y = ball_r, ball_x, ball_y
    return r, x, y

