aim = [[25, 67], [-260, -200]]

for yi in range(min(aim[1]), 300):
    for xi in range(0, max(aim[0]) + 1):
        xv, yv = xi, yi
        x = lx = y = ly = yp = 0
        while y >= min(aim[1]):
            lx, ly = x, y
            if xv > 0:
                x += xv
                xv -= 1
            y += yv
            yv -= 1
            if y > yp:
                yp = y
            if min(aim[1]) <= ly <= max(aim[1]) and min(aim[0]) <= lx <= max(aim[0]):
                print(
                    "Launch (%s,%s) reaches peak at %s and hits aim at (%s,%s)"
                    % (xi, yi, yp, lx, ly)
                )
                break
