import sys
import time
import requests
import pandas as pd
import json
import urllib
import threading
from faker import Faker

areaName = [
    "北京",
    "上海",
    "天津",
    "河北",
    "山西",
    "内蒙古",
    "吉林",
    "黑龙江",
    "江苏",
    "浙江",
    "安徽",
    "福建",
    "江西",
    "山东",
    "河南",
    "湖北",
    "湖南",
    "广东",
    "广西",
    "海南",
    "重庆",
    "四川",
    "贵州",
    "云南",
    "西藏",
    "陕西",
    "甘肃",
    "青海",
    "宁夏",
    "新疆",
    "香港",
    "澳门",
    "台湾",
]

iname = [
    "赵",
    "钱",
    "孙",
    "李",
    "周",
    "吴",
    "郑",
    "王",
    "冯",
    "陈",
    "褚",
    "卫",
    "蒋",
    "沈",
    "韩",
    "杨",
    "朱",
    "秦",
    "尤",
    "许",
    "何",
    "吕",
    "施",
    "张",
    "孔",
    "曹",
    "严",
    "华",
    "金",
    "魏",
    "陶",
    "姜",
    "戚",
    "谢",
    "邹",
    "喻",
    "柏",
    "水",
    "窦",
    "章",
    "云",
    "苏",
    "潘",
    "葛",
    "奚",
    "范",
    "彭",
    "郎",
    "鲁",
    "韦",
    "昌",
    "马",
    "苗",
    "凤",
    "花",
    "方",
    "俞",
    "任",
    "袁",
    "柳",
    "酆",
    "鲍",
    "史",
    "唐",
    "费",
    "廉",
    "岑",
    "薛",
    "雷",
    "贺",
    "倪",
    "汤",
    "滕",
    "殷",
    "罗",
    "毕",
    "郝",
    "邬",
    "安",
    "常",
    "乐",
    "于",
    "时",
    "傅",
    "皮",
    "卞",
    "齐",
    "康",
    "伍",
    "余",
    "元",
    "卜",
    "顾",
    "孟",
    "平",
    "黄",
    "和",
    "穆",
    "萧",
    "尹",
    "姚",
    "邵",
    "湛",
    "汪",
    "祁",
    "毛",
    "禹",
    "狄",
    "米",
    "贝",
    "明",
    "臧",
    "计",
    "伏",
    "成",
    "戴",
    "谈",
    "宋",
    "茅",
    "庞",
    "熊",
    "纪",
    "舒",
    "屈",
    "项",
    "祝",
    "董",
    "梁",
    "杜",
    "阮",
    "蓝",
    "闵",
    "席",
    "季",
    "麻",
    "强",
    "贾",
    "路",
    "娄",
    "危",
    "江",
    "童",
    "颜",
    "郭",
    "梅",
    "盛",
    "林",
    "刁",
    "钟",
    "徐",
    "邱",
    "骆",
    "高",
    "夏",
    "蔡",
    "田",
    "樊",
    "胡",
    "凌",
    "霍",
    "虞",
    "万",
    "支",
    "柯",
    "昝",
    "管",
    "卢",
    "莫",
    "经",
    "房",
    "裘",
    "缪",
    "干",
    "解",
    "应",
    "宗",
    "丁",
    "宣",
    "贲",
    "邓",
    "郁",
    "单",
    "杭",
    "洪",
    "包",
    "诸",
    "左",
    "石",
    "崔",
    "吉",
    "钮",
    "龚",
    "程",
    "嵇",
    "邢",
    "滑",
    "裴",
    "陆",
    "荣",
    "翁",
    "荀",
    "羊",
    "於",
    "惠",
    "甄",
    "麴",
    "家",
    "封",
    "芮",
    "羿",
    "储",
    "靳",
    "汲",
    "邴",
    "糜",
    "松",
    "井",
    "段",
    "富",
    "巫",
    "乌",
    "焦",
    "巴",
    "弓",
    "牧",
    "隗",
    "山",
    "谷",
    "车",
    "侯",
    "宓",
    "蓬",
    "全",
    "郗",
    "班",
    "仰",
    "秋",
    "仲",
    "伊",
    "宫",
    "宁",
    "仇",
    "栾",
    "暴",
    "甘",
    "钭",
    "厉",
    "戎",
    "祖",
    "武",
    "符",
    "刘",
    "景",
    "詹",
    "束",
    "龙",
    "叶",
    "幸",
    "司",
    "韶",
    "郜",
    "黎",
    "蓟",
    "薄",
    "印",
    "宿",
    "白",
    "怀",
    "蒲",
    "邰",
    "从",
    "鄂",
    "索",
    "咸",
    "籍",
    "赖",
    "卓",
    "蔺",
    "屠",
    "蒙",
    "池",
    "乔",
    "阴",
    "郁",
    "胥",
    "能",
    "苍",
    "双",
    "闻",
    "莘",
    "党",
    "翟",
    "谭",
    "贡",
    "劳",
    "逄",
    "姬",
    "申",
    "扶",
    "堵",
    "冉",
    "宰",
    "郦",
    "雍",
    "舄",
    "璩",
    "桑",
    "桂",
    "濮",
    "牛",
    "寿",
    "通",
    "边",
    "扈",
    "燕",
    "冀",
    "郏",
    "浦",
    "尚",
    "农",
    "温",
    "别",
    "庄",
    "晏",
    "柴",
    "瞿",
    "阎",
    "充",
    "慕",
    "连",
    "茹",
    "习",
    "宦",
    "艾",
    "鱼",
    "容",
    "向",
    "古",
    "易",
    "慎",
    "戈",
    "廖",
    "庾",
    "终",
    "暨",
    "居",
    "衡",
    "步",
    "都",
    "耿",
    "满",
    "弘",
    "匡",
    "国",
    "文",
    "寇",
    "广",
    "禄",
    "阙",
    "东",
    "殴",
    "殳",
    "沃",
    "利",
    "蔚",
    "越",
    "夔",
    "隆",
    "师",
    "巩",
    "厍",
    "聂",
    "晁",
    "勾",
    "敖",
    "融",
    "冷",
    "訾",
    "辛",
    "阚",
    "那",
    "简",
    "饶",
    "空",
    "曾",
    "毋",
    "沙",
    "乜",
    "养",
    "鞠",
    "须",
    "丰",
    "巢",
    "关",
    "蒯",
    "相",
    "查",
    "後",
    "荆",
    "红",
    "游",
    "竺",
    "权",
    "逯",
    "盖",
    "益",
    "桓",
    "公",
    "万俟",
    "司马",
    "上官",
    "欧阳",
    "夏侯",
    "诸葛",
    "闻人",
    "东方",
    "赫连",
    "皇甫",
    "尉迟",
    "公羊",
    "澹台",
    "公冶",
    "宗政",
    "濮阳",
    "淳于",
    "单于",
    "太叔",
    "申屠",
    "公孙",
    "仲孙",
    "轩辕",
    "令狐",
    "钟离",
    "宇文",
    "长孙",
    "慕容",
    "鲜于",
    "闾丘",
    "司徒",
    "司空",
    "亓官",
    "司寇",
    "仉",
    "督",
    "子车",
    "颛孙",
    "端木",
    "巫马",
    "公西",
    "漆雕",
    "乐正",
    "壤驷",
    "公良",
    "拓跋",
    "夹谷",
    "宰父",
    "谷梁",
    "晋",
    "楚",
    "闫",
    "法",
    "汝",
    "鄢",
    "涂",
    "钦",
    "段干",
    "百里",
    "东郭",
    "南门",
    "呼延",
    "归",
    "海",
    "羊舌",
    "微生",
    "岳",
    "帅",
    "缑",
    "亢",
    "况",
    "后",
    "有",
    "琴",
    "梁丘",
    "左丘",
    "东门",
    "西门",
    "商",
    "牟",
    "佘",
    "佴",
    "伯",
    "赏",
    "南宫",
    "墨",
    "哈",
    "谯",
    "笪",
    "年",
    "爱",
    "阳",
    "佟",
    "第五",
    "言",
    "福",
]


def get_info(num, inname, area):
    iname, icard, caseCode, areaName, disruptTypeName, publishDate = (
        [],
        [],
        [],
        [],
        [],
        [],
    )
    # url = "https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?resource_id=6899&query=%E5%A4%B1%E4%BF%A1%E8%A2%AB%E6%89%A7%E8%A1%8C%E4%BA%BA%E5%90%8D%E5%8D%95&pn=" + str(
    #     50 * num) + "&ie=utf-8&oe=utf-8&format=json"
    url = (
        "https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?resource_id=6899&query=%E5%A4%B1%E4%BF%A1%E8%A2%AB%E6%89%A7%E8%A1%8C%E4%BA%BA%E5%90%8D%E5%8D%95&cardNum=&iname="
        + inname
        + "&areaName="
        + area
        + "&pn="
        + str(num)
        + "&ie=utf-8&oe=utf-8&format=json"
    )
    # print(url)
    head = {
        "Host": "sp0.baidu.com",
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36",
        "Accept": "*/*",
        "Referer": "https://www.baidu.com/s?ie=utf-8&f=3&rsv_bp=1&tn=95943715_hao_pg&wd=%E8%80%81%E8%B5%96&oq=%25E8%2580%2581%25E8%25B5%2596&rsv_pq=ec5e631d0003d8eb&rsv_t=b295wWZB5DEWWt%2FICZvMsf2TZJVPmof2YpTR0MpCszb28dLtEQmdjyBEidZohtPIr%2FBmMrB3&rqlang=cn&rsv_enter=0&prefixsug=%25E8%2580%2581%25E8%25B5%2596&rsp=0&rsv_sug9=es_0_1&rsv_sug=9",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.8",
    }
    html = requests.get(url, headers=head).content
    html_json = json.loads(html)
    html_data = html_json["data"]
    for each in html_data:
        k = each["result"]
        for each in k:
            iname.append(each["iname"])
            icard.append(each["cardNum"])
            caseCode.append(each["caseCode"])
            areaName.append(each["areaName"])
            disruptTypeName.append(each["disruptTypeName"])
            publishDate.append(each["publishDate"])
    data = pd.DataFrame(
        {
            "name": iname,
            "IDCard": icard,
            "caseCode": caseCode,
            "areaName": areaName,
            "disruptTypeName": disruptTypeName,
            "publishDate": publishDate,
        }
    )
    data1 = data.drop_duplicates()
    data1.to_csv("a.csv", mode="a", index=False, encoding="utf-8")


if __name__ == "__main__":
    for i in areaName:
        i = urllib.parse.quote(i)
        for j in iname:
            j = urllib.parse.quote(j)
            for c in range(0, 1000, 50):
                get_info(c, j, i)
