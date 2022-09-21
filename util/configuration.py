class config:
    # 邮件发送相关
    mail_account = "发送人账号"
    mail_password = "发送人密码"
    mail_to_list = ["接收人1",]
    mail_signature = "PyBOT"
    mail_subject = "【太子钟表特约】瞬间爆地球"
    # 天气api相关
    weather_api_param_key = "天气key"
    weather_api_param_city = "440100"
    weather_api_param_extensions = "all"
    weather_api_param_url_template = "http://restapi.amap.com/v3/weather/weatherInfo?key={}&city={}&extensions={}"
    # 微博热搜api
    weibo_hot_api_url = "https://tenapi.cn/resou/"