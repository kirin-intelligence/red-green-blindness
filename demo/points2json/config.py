left_point = [116.195962, 40.055176]
right_point = [116.400582, 39.906151]
x1 = left_point[0]
y1 = left_point[1]
x_step = 0.0124
x_count = -int(((x1 - right_point[0]) // x_step) - 1)
y_step = 0.009
y_count = int(((y1 - right_point[1]) // y_step) + 1)

special_point = []
# special_point = [(0, 0)]

size = 1200
worktime = [7, 8, 17, 18,22]
spacing_time=120
