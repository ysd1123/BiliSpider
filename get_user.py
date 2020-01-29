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
    user_data = requests.get(url)
    user_data.encoding = 'utf-8'
    dict_userdata = user_data.json()
    if dict_userdata['code'] == 0:
        return dict_userdata['data']
    else:
        return 'User 404'


if __name__ == "__main__":
    pass
