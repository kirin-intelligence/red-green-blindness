
left_point = [116.204495, 39.994064]
right_point = [116.316193, 39.892346]
#left_point = [116.224495, 39.984064]

left_point = [116.250892,39.977359]
# right_point = [116.306193, 39.892346]
x1 = left_point[0]
y1 = left_point[1]
x_step = 0.0124
x_count = 0.1 // x_step
y_step = 0.009
y_count = 0.1 // y_step
size = 1200
x_count = 10
UNIT_SIZE = 1200
from redis import StrictRedis, ConnectionPool
pool = ConnectionPool(host='123.56.19.49', password='wscjxky123', port=6379, db=2)
redis = StrictRedis(connection_pool=pool)