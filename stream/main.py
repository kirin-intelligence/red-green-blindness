from report import *
from RGB_color import *
from split_dir import *
import json
from xlr import *
from xlr import write_excel

from redis import StrictRedis, ConnectionPool

pool = ConnectionPool(host='123.56.19.49', password='wscjxky123', port=6379, db=5)
redis = StrictRedis(connection_pool=pool)
if __name__ == '__main__':
    day = 'morning'
    #    # 蓟门桥
    # gps_center = [116.35716199999999, 39.971875999999995]
    # result=[[[116.35414781314877, 39.97680300729926, 0], [116.35422289965396, 39.975579467153274, 0]], [[116.35431943944634, 39.9765566569343, 1], [116.35442670588233, 39.97488968613138, 1]], [[116.35420144636676, 39.97529205839415, 1], [116.35423362629756, 39.975021072992696, 1]], [[116.35429798615915, 39.974298445255464, 1], [116.35439452595153, 39.974799357664224, 1]], [[116.35425507958476, 39.97413421167882, 1], [116.35453397231832, 39.97006943065693, 1]], [[116.36193535640136, 39.967819430656924, 1], [116.36358725951555, 39.967819430656924, 1]], [[116.3562073287197, 39.967778372262764, 1], [116.35878172318337, 39.967778372262764, 1]], [[116.35895334948096, 39.96781121897809, 1], [116.361677916955, 39.96781121897809, 1]], [[116.35346130795845, 39.967778372262764, 1], [116.3561858754325, 39.967778372262764, 1]]]

    # 西土城0
    # gps_center = [116.35716199999999,39.980875999999995]
    # result=[[[116.35377238062281, 39.98500647445255, 0], [116.35396546020759, 39.98229662043795, 0]], [[116.35368656747403, 39.98451377372262, 0], [116.35399764013839, 39.97989881021897, 0]], [[116.35405127335639, 39.98117983211678, 0], [116.35415853979237, 39.979463591240865, 0]], [[116.35360075432524, 39.985581291970796, 1], [116.35366511418684, 39.98455483211678, 1]], [[116.35342912802767, 39.98489972262773, 1], [116.35342912802767, 39.985334941605835, 1]], [[116.3539869134948, 39.982280197080286, 1], [116.35404054671278, 39.98139333576641, 1]], [[116.36188172318337, 39.98134406569342, 1], [116.36188172318337, 39.98167253284671, 1]], [[116.3539869134948, 39.980375087591234, 1], [116.35407272664358, 39.9805968029197, 1]], [[116.35416926643597, 39.97859315328466, 1], [116.35430871280275, 39.976581291970795, 1]], [[116.35410490657438, 39.977123262773716, 1], [116.35417999307957, 39.975957204379554, 1]], [[116.35429798615915, 39.97656486861313, 1], [116.35437307266434, 39.975957204379554, 1]]]

    # 六道口
    # gps_center = [116.35716199999999,39.998875999999996]

    #    # 紫竹桥
    gps_center = [116.30756199999999, 39.944875999999994]
    #
    input_dir = '/run/media/kirin/新加卷/server/'
    target_dir = '/run/media/kirin/新加卷1/images/'
    # spilt_file(input_dir, target_dir)
    # print(day)
    rgb_img = run_rgb(target_dir, day, gps_center)
    result = report(rgb_img, gps_center)
    print(result)
    img = cv2.imread("out_put.png")
    # result=[[[116.35377238062281, 39.98500647445255, 0], [116.35396546020759, 39.98229662043795, 0]], [[116.35368656747403, 39.98451377372262, 0], [116.35399764013839, 39.97989881021897, 0]], [[116.35405127335639, 39.98117983211678, 0], [116.35415853979237, 39.979463591240865, 0]], [[116.35360075432524, 39.985581291970796, 1], [116.35366511418684, 39.98455483211678, 1]], [[116.35342912802767, 39.98489972262773, 1], [116.35342912802767, 39.985334941605835, 1]], [[116.3539869134948, 39.982280197080286, 1], [116.35404054671278, 39.98139333576641, 1]], [[116.36188172318337, 39.98134406569342, 1], [116.36188172318337, 39.98167253284671, 1]], [[116.3539869134948, 39.980375087591234, 1], [116.35407272664358, 39.9805968029197, 1]], [[116.35416926643597, 39.97859315328466, 1], [116.35430871280275, 39.976581291970795, 1]], [[116.35410490657438, 39.977123262773716, 1], [116.35417999307957, 39.975957204379554, 1]], [[116.35429798615915, 39.97656486861313, 1], [116.35437307266434, 39.975957204379554, 1]]]
    # write_excel(result, day)
    # write_html(gps_center, result)
    cv2.imshow('a', img)
    cv2.waitKey(0)
    #     redis_key="%s:%s_%s"%(day,gps_center[0],gps_center[1])
    #     results= [[[116.35431943944634, 39.9765566569343, 0], [116.35443743252593, 39.97489789781021, 0]], [[116.35124089273354, 39.97656486861313, 0], [116.3531073287197, 39.97656486861313, 0]], [[116.36234296885812, 39.97658950364963, 0], [116.36358725951555, 39.97658950364963, 0]], [[116.3601654602076, 39.97650738686131, 0], [116.361677916955, 39.97650738686131, 0]], [[116.36169937024219, 39.9765320218978, 0], [116.36230006228372, 39.97650738686131, 0]], [[116.35072601384081, 39.97646632846715, 0], [116.35332186159168, 39.97646632846715, 0]], [[116.35429798615915, 39.974298445255464, 0], [116.35439452595153, 39.974799357664224, 0]], [[116.35425507958476, 39.97413421167882, 0], [116.35453397231832, 39.97006943065693, 0]], [[116.35266753633216, 39.96804935766423, 0], [116.35297860899652, 39.96867344525547, 0]], [[116.35497376470586, 39.96859132846715, 0], [116.35587480276814, 39.968238226277364, 0]], [[116.35134815916953, 39.967786583941596, 0], [116.36201044290655, 39.967786583941596, 0]], [[116.35346130795845, 39.967663408759115, 0], [116.35599279584774, 39.967663408759115, 0]], [[116.35673293425604, 39.967663408759115, 0], [116.3585457370242, 39.967663408759115, 0]], [[116.35072601384081, 39.967663408759115, 0], [116.35343985467127, 39.967663408759115, 0]], [[116.36275058131486, 39.9675566569343, 0], [116.36358725951555, 39.9675566569343, 0]], [[116.35420144636676, 39.975300270072985, 1], [116.35428725951556, 39.97415884671532, 1]], [[116.35295715570932, 39.96871450364963, 1], [116.3531716885813, 39.969231839416054, 1]]]
    #     for i in results:
    #         redis.lpush(redis_key,json.dumps(i))
