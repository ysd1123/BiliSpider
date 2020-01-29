'''
内置 data() 函数，以字典形式返回参数 uuid 所对应的Bilibili 用户的数据。
mid：uuid
following：关注
whisper：？
black：黑名单
follower：粉丝
'''

import requests


def data(uuid):
    url = 'https://api.bilibili.com/x/relation/stat?vmid='+str(uuid)
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
    user_data = requests.get(url, headers=headers)
    user_data.encoding = 'utf-8'
    dict_userdata = user_data.json()

    if dict_userdata['code'] == 0:
        return dict_userdata['data']
    else:
        return 'User 404'


if __name__ == "__main__":
    pass
