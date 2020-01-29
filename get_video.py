'''
内置 data() 函数，以字典形式返回参数 aid 所对应的Bilibili av号的视频数据。
aid：av号
view：播放
danmaku：弹幕
reply：评论
favorite：收藏
coin：投币
share：分享
now_rank：？
his_rank：？
like：点赞
dislike：？
no_reprint：？
copyright：版权信息（1代表自制，2代表转载）
'''

import requests


def data(aid):
    url = 'https://api.bilibili.com/archive_stat/stat?aid='+str(aid)
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
    av_data = requests.get(url, headers=headers)
    av_data.encoding = 'utf-8'
    dict_avdata = av_data.json()

    if dict_avdata['code'] == 0:
        return dict_avdata['data']
    else:
        return 'Video 404'


if __name__ == "__main__":
    pass
