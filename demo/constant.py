import os
# 分析的数据包含的天数
DATA_CONTAIN_DAYS='data_contain_days'
WORK_TIME = 'work_time'
LEFT_POINT = 'left_point'
RIGHT_POINT = 'right_point'
#间隔时间
SPACING_TIME = 'spacing_time'
GLOBAL_CONFIG = {}
TIME_WEIGHT = 'time_weight'
SAVE_PATH = 'save_path'
CHOOSE_ROAD='choose_road'
THREAD_FLAG = 'thread_flag'
ROAD_DATAS = ["全部", "德胜门外大街","西外大街","学院路","万泉河路","阜石路","紫竹院路","三环路","二环路"]
EXCEL_DIR = 'excel_dir'

STOP='stop'
ERROR='error'
SUCCESS = 'success'
DATA_DIR = 'data_dir'
# 工作日爬不爬，只爬工作日
ONLY_WORK_DAY='only_walk_day'
# dayOfWeek = datetime.datetime.now().weekday()
# 去掉工作日
ALPHA = 0.8
BELTA = 0.5
GAMA = 0.3
SOCKET_TIMEOUT = 25

JSON_FILE_PATH='lib/static/data.json'
JSON_NO='no'
JSON_START_POINT='start_point'
JSON_END_POINT='end_point'
JSON_END_PLACE='end_place'
JSON_START_PLACE='start_place'
JSON_DAY='day'
JSON_DISTANCE='distance'
JSON_PATHS='paths'
JSON_TYPE='type'
JSON_JAM_TIME='jam_time'
JSON_TEMPLATE = ['no', 'start_point', 'start_place', 'end_point'
    , 'end_place', 'day', 'distance', 'paths', 'type', 'jam_time']
WRONG_POINT_ARR=[125,]

CWD = os.getcwd()
APP_ImagePath = CWD + os.sep + 'image'
APP_HtmlPath = CWD + os.sep + 'lib'
GAODE_KEY = '2be4c36d53e74e0c585326d62d6fe6e3'



Svg_icon_loading = '''<svg width="100%" height="100%" viewBox="0 0 38 38" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient x1="8.042%" y1="0%" x2="65.682%" y2="23.865%" id="a">
            <stop stop-color="#03a9f4" stop-opacity="0" offset="0%"/>
            <stop stop-color="#03a9f4" stop-opacity=".631" offset="63.146%"/>
            <stop stop-color="#03a9f4" offset="100%"/>
        </linearGradient>
    </defs>
    <g fill="none" fill-rule="evenodd">
        <g transform="translate(1 1)">
            <path d="M36 18c0-9.94-8.06-18-18-18" id="Oval-2" stroke="url(#a)" stroke-width="2">
                <animateTransform
                    attributeName="transform"
                    type="rotate"
                    from="0 18 18"
                    to="360 18 18"
                    dur="0.5s"
                    repeatCount="indefinite" />
            </path>
            <circle fill="#03a9f4" cx="36" cy="18" r="4">
                <animateTransform
                    attributeName="transform"
                    type="rotate"
                    from="0 18 18"
                    to="360 18 18"
                    dur="0.5s"
                    repeatCount="indefinite" />
            </circle>
        </g>
    </g>
</svg>'''.encode()

