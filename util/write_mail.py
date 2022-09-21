import json
import markdown
import datetime

all_content_template = '''
### 🗞︎🗞︎🗞︎ 天气小预报 🌏🌏🌏

### ⏰ {todayDate} {weekday}

****
## 当前天气 {todayWeather}
{todayMsg}


## 明日天气
{tomorrowMsg}


## 未来趋势
{futureTrend}

****
## 微博热搜
{hotWeibo}
'''

hot_weibo_template = "- 🔥{hot}【[{name}]({url})】"

weekDict = {
    "1": "星期一",
    "2": "星期二",
    "3": "星期三",
    "4": "星期四",
    "5": "星期五",
    "6": "星期六",
    "7": "星期日"
}

def assembleMarkdownContent(weatherDict,hotList):
    # 微博热搜处理成段落
    hotWeibo = assembleHotWeiboToParagraph(hotList)
    # 再处理天气
    # 1.取今日
    todayDate = datetime.date.today()
    todayInfo = weatherDict[todayDate.strftime("%Y-%m-%d")]
    weekDay = weekDict[todayInfo["week"]]
    todayMsg = todayInfo["dayweather"] + "转" + todayInfo["nightweather"] + "；早间气温" + todayInfo["daytemp"] + "℃；晚间气温" + todayInfo["nighttemp"] + "℃"
    # 2.取明日
    tomorrowDate = todayDate + datetime.timedelta(days=1)
    tomorrowInfo = weatherDict[tomorrowDate.strftime("%Y-%m-%d")]
    tomorrowMsg = tomorrowInfo["dayweather"] + "转" + tomorrowInfo["nightweather"] + "；早间气温" + tomorrowInfo["daytemp"] + "℃；晚间气温" + tomorrowInfo["nighttemp"] + "℃"
    # 3.取未来（后日和大后日）
    nextTomorrowDate = tomorrowDate + datetime.timedelta(days=1)
    bigNextTomorrowDate = nextTomorrowDate + datetime.timedelta(days=1)
    nextTomorrowInfo = weatherDict[nextTomorrowDate.strftime("%Y-%m-%d")]
    bigNextTomorrowInfo = weatherDict[bigNextTomorrowDate.strftime("%Y-%m-%d")]
    futureTrend = "未来第三日开始天气由" + nextTomorrowInfo["dayweather"] + "转" + bigNextTomorrowInfo["nightweather"]
    # 4.填充模板
    afterFill = all_content_template.format(todayDate=todayDate,weekday=weekDay,todayWeather=todayInfo["dayweather"],todayMsg=todayMsg,tomorrowMsg=tomorrowMsg,futureTrend=futureTrend,hotWeibo=hotWeibo)
    # 5.markdown转html
    return markdown.markdown(afterFill)

def assembleHotWeiboToParagraph(hotList):
    paragraph = ""
    for hotItem in hotList:
        paragraph = paragraph + hot_weibo_template.format(hot=hotItem["hot"],name=hotItem["name"],url=hotItem["url"]) + "\n"
    return paragraph

if __name__ == '__main__':
    tempDict = {"2022-09-08": {"date": "2022-09-08", "week": "4", "dayweather": "中雨", "nightweather": "雷阵雨", "daytemp": "33", "nighttemp": "25", "daywind": "北", "nightwind": "北", "daypower": "≤3", "nightpower": "≤3"}, "2022-09-09": {"date": "2022-09-09", "week": "5", "dayweather": "雷阵雨", "nightweather": "多云", "daytemp": "33", "nighttemp": "25", "daywind": "北", "nightwind": "北", "daypower": "≤3", "nightpower": "≤3"}, "2022-09-10": {"date": "2022-09-10", "week": "6", "dayweather": "雷阵雨", "nightweather": "多云", "daytemp": "33", "nighttemp": "25", "daywind": "北", "nightwind": "北", "daypower": "≤3", "nightpower": "≤3"}, "2022-09-11": {"date": "2022-09-11", "week": "7", "dayweather": "雷阵雨", "nightweather": "多云", "daytemp": "33", "nighttemp": "24", "daywind": "北", "nightwind": "北", "daypower": "≤3", "nightpower": "≤3"}}
    print(assembleMarkdownContent(tempDict))
