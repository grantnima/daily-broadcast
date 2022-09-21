import requests
import json
from util.configuration import config

def getHotWeibo():
    # 请求Tenapi的微博热搜接口
    try:
        response = requests.get(config.weibo_hot_api_url)
        responseObj = json.loads(response.text)
    except Exception as ex:
        raise Exception("微博热搜接口请求异常,response: {}".format(response))
    if ("data" in responseObj and responseObj["data"] != 200) or ("list" not in responseObj):
        raise Exception("微博热搜接口请求异常,rawResponse: {}".format(responseObj))
    else:
        return responseObj["list"]

