# config.py 自定义配置
import os
import re

"""
github action部署或本地部署
从环境变量获取值,如果不存在使用默认本地值
每一次代表30秒，比如你想刷1个小时这里填120，你只需要签到这里填2次
"""

# 阅读次数 默认120次/60分钟
READ_NUM = int(os.getenv('READ_NUM', '120'))
# pushplus、wxpusher、telegram
PUSH_METHOD = "" or os.getenv('PUSH_METHOD')
# pushplus
PUSHPLUS_TOKEN = "" or os.getenv("PUSHPLUS_TOKEN")
# telegram
TELEGRAM_BOT_TOKEN = "" or os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = "" or os.getenv("TELEGRAM_CHAT_ID")
# wxpusher
WXPUSHER_SPT = "" or os.getenv("WXPUSHER_SPT")
# 复制的curl_bath命令
curl_str = os.getenv('WXREAD_CURL')

# 对应替换
headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9",
    "baggage": "sentry-environment=production,sentry-release=dev-1743080809165,sentry-public_key=ed67ed71f7804a038e898ba54bd66e44,sentry-trace_id=5c2514ee3fda4391a9905535f5d744b5",
    "cache-control": "no-cache",
    "content-type": "application/json;charset=UTF-8",
    "dnt": "1",
    "origin": "https://weread.qq.com",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://weread.qq.com/web/reader/bd6323f0813ab7379g017d4f",
    "sec-ch-ua": "\"Microsoft Edge\";v=\"129\", \"Not=A?Brand\";v=\"8\", \"Chromium\";v=\"129\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "sentry-trace": "5c2514ee3fda4391a9905535f5d744b5-afe8adb4785ce2a1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0"
}
#
# #对应替换
cookies = {
    'pgv_pvid': '1344205172',
    'RK': '2SV0aGTGZ9',
    'ptcz': '993f1995ebb6ba0389893b485608422dbc00e7af202e806fc1f5d69d0dc1b4fe',
    'pac_uid': '0_m8JBCKtSDjrSh',
    '_qimei_uuid42': '18617141c071001af9810ca46f4d006c64b624a3c2',
    '_qimei_q32': 'e20e8fc5d81916ff887e0e600ec71dc5',
    '_qimei_q36': 'd3b5484ddc04b69637a4240f30001b318615',
    '_qimei_h38': '19c5d0e8f9810ca46f4d006c0200000c918617',
    'suid': 'user_0_m8JBCKtSDjrSh',
    'qq_domain_video_guid_verify': '55f080bee1062fbc',
    'o_cookie': '862034684',
    'fqm_pvqid': '3d142ae5-1a22-42b3-b82c-0ee2d11da66c',
    'eas_sid': 'N1x7s4H1K3P4a23023S6J1G5F7',
    '_ga_RPMZTEBERQ': 'GS1.1.1742477209.1.1.1742477284.0.0.0',
    '_ga': 'GA1.2.70145830.1742477209',
    '_ga_6WSZ0YS5ZQ': 'GS1.1.1742477370.1.1.1742478360.0.0.0',
    '_qimei_fingerprint': '44da70c2216c13ffda8a9e8a21ce2ac6',
    'current-city-name': 'sz',
    'wr_vid': '408861837',
    'wr_rt': 'web%40fvNw5lqtuuQwfmYOlFe_AL',
    'wr_localvid': '86c324208185ebc8d86c526',
    'wr_name': 'Icecoldtime',
    'wr_avatar': 'https%3A%2F%2Fthirdwx.qlogo.cn%2Fmmopen%2Fvi_32%2FPOgEwh4mIHO4nibH0KlMECNjjGxQUq24ZEaGT4poC6icRiccVGKSyXwibcPq4BWmiaIGuG1icwxaQX6grC9VemZoJ8rg%2F132',
    'wr_gender': '0',
    'wr_pf': 'NaN',
    'wr_theme': 'dark',
    'uin': 'o0862034684',
    'skey': '@XUss96sFt',
    'pgv_info': 'ssid=s8122873432',
    'rv2': '8020DF97E9AB05E542071D3B58527C22B6CD3E3C24FF8814AD',
    'property20': '69E044A6AB5447C839959C32E631498ED1F7990CE9A6B0651F76B29FF617F0793D02EE8546D5D381',
    'wr_gid': '219257733',
    'wr_fp': '306301264',
    'wr_skey': 'nm6NRTjo',
}

# 保留| 默认读三体，其它书籍自行测试时间是否增加
data = {
    'appId': 'wb182564874663h1964571299',
    'b': 'bd6323f0813ab7379g017d4f',
    'c': '1c3321802231c383cd30bb3',
    'ci': 35,
    'co': 3005,
    'sm': '看，下面的情况是可能的：资本家曾经一度依',
    'pr': 27,
    'rt': 120,
    'ts': 1743305927589,
    'rn': 824,
    'sg': '7eb53d20e7dc0fc45c0f65eba8f917d6c4bc7a590d41f73023d72f8100594c89',
    'ct': 1743305927,
    'ps': 'bf8329307a64126ag0150bd',
    'pc': '728321007a641265g015149',
    's': '79cbe392',
}


def convert(curl_command):
    """提取headers与cookies"""
    # 提取 headers
    for match in re.findall(r"-H '([^:]+): ([^']+)'", curl_command):
        headers[match[0]] = match[1]

    # 提取 cookies
    cookies = {}
    cookie_string = headers.pop('cookie', '')
    for cookie in cookie_string.split('; '):
        key, value = cookie.split('=', 1)
        cookies[key] = value

    return headers, cookies


headers, cookies = convert(curl_str) if curl_str else (headers, cookies)
