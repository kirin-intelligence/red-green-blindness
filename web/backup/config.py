
GLOBAL_CONFIG[LEFT_POINT] = [116.204495, 39.994064]
#GLOBAL_CONFIG[LEFT_POINT] = [116.224495, 39.984064]

GLOBAL_CONFIG[LEFT_POINT] = [116.195962,40.025876]
GLOBAL_CONFIG[RIGHT_POINT] = [116.400582,39.906151]
x1 = GLOBAL_CONFIG[LEFT_POINT][0]
y1 = GLOBAL_CONFIG[LEFT_POINT][1]
x_step = 0.0124
x_count = -int(((x1-GLOBAL_CONFIG[RIGHT_POINT][0]) // x_step) -1)
y_step = 0.009
y_count = int(((y1-GLOBAL_CONFIG[RIGHT_POINT][1]) // y_step)+1)
size = 1200

UNIT_SIZE = 1200
from redis import StrictRedis, ConnectionPool
pool = ConnectionPool(host='123.56.19.49', password='wscjxky123', port=6379, db=2, decode_responses=True)
redis = StrictRedis(connection_pool=pool)