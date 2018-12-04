import requests
import re
import os
import urllib

print("此方法无法下载已下架和需单独购买歌曲！")
print("所下载歌曲版权归网易所有，请勿用于商业用途，且需在24小时内删除，否则后果自负！")
print("软件代码版权所有，严禁侵犯！")
print()
while True:
    oldUrl = input("请复制网易云歌曲地址，如：https://music.163.com/#/song?id=413812473\n地址：") #https://music.163.com/#/song?id=228252
    print()
    if "&" in oldUrl:
        songIds = re.findall("id=(.*[0-9])&",oldUrl)
    else:
        songIds = re.findall("id=(.*[0-9])",oldUrl)
    songId = songIds[0]
    nameUrl = f"http://music.163.com/api/song/detail/?id={songId}&ids=%5B{songId}%5D"
    headers = {
        'Cookie': '''_ntes_nnid=b71ffe36e46af75f1d79299195dcb1fb,1535714747971; _ntes_nuid=b71ffe36e46af75f1d79299195dcb1fb; _iuqxldmzr_=32; WM_TID=SCg4H5LsBItBVVFAVVN8aVNQaPCVEvuf; __utmz=94650624.1540643279.10.5.utmcsr=cnblogs.com|utmccn=(referral)|utmcmd=referral|utmcct=/; P_INFO=discretemath16@126.com|1540713894|0|other|00&99|jis&1540690871&mail126#jis&320100#10#0#0|&0|urs&mail126|discretemath16@126.com; mail_psc_fingerprint=1964e5031818834ef725f65ba0cae890; vjuids=1a9b40d72.166dc2f95e1.0.54d6d59e1d308; vinfo_n_f_l_n3=a2a7dd60a756b516.1.11.1536064453105.1539960122601.1541292440311; vjlast=1541292398.1542459367.13; __f_=1543742942721; JSESSIONID-WYYY=HxXcHXnREmjb9qfSbID9VoEJrEWkrZ%2BZhK%2F7iUzrSIg1CaX3nJVAHtS3qPHtZ%5CERhyE%2FJxhRiaNpA7Qov%5Ci9WMRz%5CtNzNDkZNij6Gal%2BiJpb05ZcFvuI2Vt7b4k%2Bsi9F2%5C3Mj7EnlPzqaAuj1GhChyNwlG8s5UhiXNf3qSgov4MeKloB%3A1543909236540; __utma=94650624.952492931.1537873835.1540643279.1543907437.11; __utmc=94650624; WM_NI=VBMWIdpTsOvrSus0Al63z7rdV5MuOaR4zgvpL%2FdewFf88pWwoBULOnzUU3N%2BJ7DF0zDUMBVZsH4Vhm%2FSYgi4%2FmTCT4aDzuU8ufqryOtKgZal84rv1Ua1m4md%2FIOCjZmmNEM%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee87ea4792b0b88af053fc928fb2c14b868e8ebbbc6abbaa8ab6ca45f8f5f8b7aa2af0fea7c3b92a969e83b8cc70b48cbdb0f57a91abbdd1c468f6edb6d8f17096eb8396ce6b92ecb688f57c90f1ac86f64ea6e8f891d67dad9e9badce66ba8b9bd4cd218ae98ca7b372888b83a3d552b198fcb7eb67ed8d9788ec40edb39ca4d740a39cb696d834b7babf93fc45b895a9bbe468fcecbe97b45fa3efa3d5f070ed9781a4e952afb382a6d037e2a3; __utmb=94650624.9.10.1543907437''',
        'User-Agent': '''Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'''
    }

    html = requests.get(nameUrl,headers = headers).text

    names = re.findall('''"name":"(.*?)"''',html)
    name = names[0]
    artist = names[1]

    print()
    print(f"已检测到歌曲：{name}-{artist}")
    newUrl = f"http://music.163.com/song/media/outer/url?id={songId}.mp3"  #http://music.163.com/song/media/outer/url?id=228252.mp3
    songHtml = requests.get(newUrl,headers = headers,allow_redirects=False)

    if songHtml.url == "https://music.163.com/404" or songHtml.url == "http://music.163.com/404":
        print("下载失败，无法下载！请检查歌曲是否需付费")
    else:
        print("正在下载...")
        newNewUrl = songHtml.headers['location']
        if newNewUrl == "https://music.163.com/404" or newNewUrl == "http://music.163.com/404":
            print("下载失败，无法下载！请检查歌曲是否需付费")
        else:
            urllib.request.urlretrieve(newNewUrl, f"{name}-{artist}.mp3")
            print("下载完成！")
    print()
    print()
