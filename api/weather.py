import requests
import json
from util.configuration import config

def assembleUrl():
    return config.weather_api_param_url_template.format(config.weather_api_param_key,config.weather_api_param_city,config.weather_api_param_extensions)

def getWeather(url):
    # 请求高德api
    response = requests.get(url)
    responseObj = json.loads(response.text)
    if "status" in responseObj and responseObj["status"] != '1':
        raise Exception("天气接口请求异常,rawResponse: {}".format(responseObj))
    else:
        return responseObj

def assembleDict(responseObj):
    # 规整成存储的格式 -> hash field:日期 value: 全部信息
    # 1.获取天气信息 判空
    if "forecasts" not in responseObj:
        raise Exception("天气接口返回预报信息为空,rawResponse: {}".format(responseObj))
    forecastList = responseObj["forecasts"]
    # 2.初始化字典
    toCacheDict = {}
    # 3.遍历forecastList 目前只查广州 里面只有一个元素
    for forecast in forecastList:
        if "casts" not in forecast:
            raise Exception("天气接口返回预报信息为空,rawResponse: {}".format(responseObj))
        castList = forecast["casts"]
        # 4.遍历castList 里面有当日和未来三日共四个元素
        for cast in castList:
            # 5.塞进toCacheDict
            toCacheDict[cast["date"]] = cast
    # 6.return
    print(toCacheDict)
    return toCacheDict

def getWeatherDict():
    return assembleDict(getWeather(assembleUrl()))

if __name__ == "__main__":
    try:
        assembleDict(getWeather(assembleUrl()))
    except Exception as ex:
        print("request weather fail,err: {}".format(ex))