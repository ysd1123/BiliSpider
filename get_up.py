'''
内置 data() 函数，以字典形式返回参数 uuid 所对应的Bilibili 用户的数据。
video_view：视频浏览
article_view：文章浏览
like：总点赞
'''

import requests


def data(uuid):
    url = 'https://api.bilibili.com/x/space/upstat?mid='+str(uuid)
    Up_data = requests.get(url)
    Up_data.encoding = 'utf-8'
    dict_Updata = Up_data.json()
    if dict_Updata['code'] == 0:
        #return dict_Updata['data']
    else:
        return 'Up 404'


if __name__ == "__main__":
    pass
