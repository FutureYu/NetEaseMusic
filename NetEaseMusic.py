import requests
import re
import os
import urllib

print("此方法无法下载已下架和需单独购买歌曲")
print("所下载歌曲版权归网易所有，请勿用于商业用途，否则后果自负")
print("软件代码版权所有，严禁侵犯")
print()
while True:
    oldUrl = input("请复制网易云歌曲地址，如：https://music.163.com/#/song?id=413812473\n地址：") #https://music.163.com/#/song?id=228252
    print()
    songIds = re.findall("id=(.*[0-9])",oldUrl)
    songId = songIds[0]
    nameUrl = f"http://music.163.com/api/song/detail/?id={songId}&ids=%5B{songId}%5D"
    headers = {
        'Cookie': '''__f_=1535714748410; _ntes_nnid=b71ffe36e46af75f1d79299195dcb1fb,1535714747971; _ntes_nuid=b71ffe36e46af75f1d79299195dcb1fb; P_INFO=13513673164|1536330039|0|ydaq_web|00&99|null&null&null#jis&null#10#0#0|&0|null|13513673164; _iuqxldmzr_=32; WM_TID=SCg4H5LsBItBVVFAVVN8aVNQaPCVEvuf; vinfo_n_f_l_n3=a2a7dd60a756b516.1.7.1536064453105.1539087711502.1539687814569; __utmc=94650624; __utmz=94650624.1539775406.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic|utmctr=%E7%BD%91%E6%98%93%E4%BA%91; playerid=98072337; __utma=94650624.952492931.1537873835.1539777821.1539781919.4; WM_NI=rpHMEY1e%2B4XArYAn0f%2F7c9z9sZKzvx4CmCfYGDdvQXflqu6rsGAI8tyBx4EDIVr4J0qgt9C2iqOtOheCTDVOV%2FiXn44c3Bz8uuNs6zbPBboUr0NYbzij1C3t5mxDajuwdnc%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee8ce579b09f8ca4dc50a39e8fb6c84a838b9aaab7488f9f86aad63af2f5a7acc52af0fea7c3b92ab2b088aec853f3bbe5d5db4bb2878f8fb36eede9addaf933b186859bf574f89da3a4e553859cac97d454a6b4bf96b57ab1998faabb80bb9eb8d5c8508b8abed5c93cb3b9bcdac23aabaf8195ce64a79d9ca5d54596f1a7b9ed40f8bdfda3f934b7ab8294b572a2908e83ee5fb2f082bae172abb6ffa4b280f7b3b8a5e462b7a9ac8fe237e2a3; JSESSIONID-WYYY=J10kl%2Bq729ZO8mGGU7GO4M54Pb1C0ePi8HflIg9%5CUuag8AU5y2Ym6fM3VTvKJJ%2FAV0DM3yh7A%2BHFb2B8HWUbMoK%2FcktuQRrMvwXjMq1yFPeRzxj8IrwdCo930p8xI%5CQgttbqUMP9tfzbveeYEFQyTJPCS4Of5CFPq%5CEERCaa1xd9Xnnu%3A1539787650118; __utmb=94650624.36.10.1539781919''',
        'User-Agent': '''Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'''
    }

    html = requests.get(nameUrl,headers = headers).text

    names = re.findall('''"name":"(.*?)"''',html)
    name = names[0]
    artist = names[1]

    print()
    print(f"已检测到歌曲：{name}-{artist}")
    print("正在下载...")
    print()

    newUrl = f"http://music.163.com/song/media/outer/url?id={songId}.mp3"  #http://music.163.com/song/media/outer/url?id=228252.mp3
    urllib.request.urlretrieve(newUrl, f"{name}-{artist}.mp3")
    print("下载完成")
    print()
    print()
