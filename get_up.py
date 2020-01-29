'''
内置 data() 函数，以字典形式返回参数 uuid 所对应的Bilibili 用户的数据。
video_view：视频浏览
article_view：文章浏览
like：总点赞
'''

import requests


def data(uuid):
    def be_simple(orig_dict):
        simple_dict = {'video_view': orig_dict['archive']['view'],
                       'article_view': orig_dict['article']['view'],
                       'likes': orig_dict['likes']}
        return simple_dict
 
    url = 'https://api.bilibili.com/x/space/upstat?mid='+str(uuid)
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
    Up_data = requests.get(url, headers=headers)
    Up_data.encoding = 'utf-8'
    dict_Updata = Up_data.json()

    if dict_Updata['code'] == 0:
        return be_simple(dict_Updata['data'])
    else:
        return 'Up 404'


if __name__ == "__main__":
    pass
