from api import weather
from api import weibo_hot
from util import write_mail
from util import send_mail

if __name__ == '__main__':
    try:
        # 1.先天气
        weatherDict = weather.getWeatherDict()
        print("天气情况获取完毕")
        # 2.获取微博微搜
        hotWeiboList = weibo_hot.getHotWeibo()
        print("微博热搜获取完毕")
        # 游民星空
        # 知乎
        # 百度热点
        # 汽车
        # 3.组装内容成html
        mailContent = write_mail.assembleMarkdownContent(weatherDict,hotWeiboList)
        print("邮件内容组装完毕")
        # 4.发送邮件
        s = send_mail.sender()
        s.doSend(mailContent)
        print("邮件发送完毕")
    except Exception as ex:
        raise Exception("广播失败, err: {}".format(ex))