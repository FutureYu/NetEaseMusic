import requests
import re
import os
import urllib
import json
import time



def downLoad(songId):
    nameUrl = f"http://music.163.com/api/song/detail/?id={songId}&ids=%5B{songId}%5D"
    headers = {
        #'Cookie': '''_ntes_nnid=b71ffe36e46af75f1d79299195dcb1fb,1535714747971; _ntes_nuid=b71ffe36e46af75f1d79299195dcb1fb; _iuqxldmzr_=32; WM_TID=SCg4H5LsBItBVVFAVVN8aVNQaPCVEvuf; mail_psc_fingerprint=1964e5031818834ef725f65ba0cae890; vjuids=1a9b40d72.166dc2f95e1.0.54d6d59e1d308; __utma=94650624.952492931.1537873835.1543912868.1543924680.14; __utmz=94650624.1543924680.14.7.utmcsr=baidu|utmccn=(organic)|utmcmd=organic|utmctr=%E7%BD%91%E6%98%93%E4%BA%91; vjlast=1541292398.1544849806.11; P_INFO=futur1yu@163.com|1548150151|1|study|00&99|bej&1547960117&moneykeeper#shx&140200#10#0#0|185352&0|moneykeeper|futur1yu@163.com; vinfo_n_f_l_n3=a2a7dd60a756b516.1.14.1536064453105.1548837064910.1552178603733; JSESSIONID-WYYY=zpsZyCW1SgVTJJOnpzt9wOWT0TYwwD3jtk%2B5MQIqgDA3ZHwYBotixxK%2FR78zb7n%5CqTVqhMq1Tua4X8h6b2TlGlUIwl57MWznt%2FD8ktok%5C8Uijdw0fU%2FHduguZ%2FkwkavrCl2pt8%2Fo0knsX3M2zMori2fbjZomv7%2BesO1dXzpp4mO1%5C95q%3A1555502848481; WM_NI=grrOIXIFEptI%2BOnfKdf1JoK19Vux2czk5aksUZRWsYV6moqkgiOhr0NXsP%2F4WKorC8GI2KIfU8UFnbfDt7h3aREUSVZI0VWfhtwMbvK9N6SEgvCMT%2BJjcR8BUVBvm%2BwyYU4%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeaad27c9392ae85d765f2e78bb6d54a978b9faff26293edafa2ed3ce9b7a9a6f62af0fea7c3b92aa5aebeb0cc548b9a8b91f743e991a287ca70a6ef8690ca3bfb8abb99b169bab5fb82ea7997869eb8f25396eaa390f461a5b78189f13c8e88bdb1ae409595a193c2348597feaccc6e97e89ba7ed6aa69cbcd8eb39a38e8bb6d25e9a9700b7d66eacacb9aee17e89e782d7d24fa5aa8daed7218ab6adb3bb4a978a8e97f021b5a797b6b737e2a3''',
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

def getSongs(playList):
    playListUrl = f"https://music.163.com/m/playlist?id={playList}"
    headers = {
        #'Cookie': '''_ntes_nnid=b71ffe36e46af75f1d79299195dcb1fb,1535714747971; _ntes_nuid=b71ffe36e46af75f1d79299195dcb1fb; _iuqxldmzr_=32; WM_TID=SCg4H5LsBItBVVFAVVN8aVNQaPCVEvuf; mail_psc_fingerprint=1964e5031818834ef725f65ba0cae890; vjuids=1a9b40d72.166dc2f95e1.0.54d6d59e1d308; __utma=94650624.952492931.1537873835.1543912868.1543924680.14; __utmz=94650624.1543924680.14.7.utmcsr=baidu|utmccn=(organic)|utmcmd=organic|utmctr=%E7%BD%91%E6%98%93%E4%BA%91; vjlast=1541292398.1544849806.11; P_INFO=futur1yu@163.com|1548150151|1|study|00&99|bej&1547960117&moneykeeper#shx&140200#10#0#0|185352&0|moneykeeper|futur1yu@163.com; vinfo_n_f_l_n3=a2a7dd60a756b516.1.14.1536064453105.1548837064910.1552178603733; JSESSIONID-WYYY=zpsZyCW1SgVTJJOnpzt9wOWT0TYwwD3jtk%2B5MQIqgDA3ZHwYBotixxK%2FR78zb7n%5CqTVqhMq1Tua4X8h6b2TlGlUIwl57MWznt%2FD8ktok%5C8Uijdw0fU%2FHduguZ%2FkwkavrCl2pt8%2Fo0knsX3M2zMori2fbjZomv7%2BesO1dXzpp4mO1%5C95q%3A1555502848481; WM_NI=grrOIXIFEptI%2BOnfKdf1JoK19Vux2czk5aksUZRWsYV6moqkgiOhr0NXsP%2F4WKorC8GI2KIfU8UFnbfDt7h3aREUSVZI0VWfhtwMbvK9N6SEgvCMT%2BJjcR8BUVBvm%2BwyYU4%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeaad27c9392ae85d765f2e78bb6d54a978b9faff26293edafa2ed3ce9b7a9a6f62af0fea7c3b92aa5aebeb0cc548b9a8b91f743e991a287ca70a6ef8690ca3bfb8abb99b169bab5fb82ea7997869eb8f25396eaa390f461a5b78189f13c8e88bdb1ae409595a193c2348597feaccc6e97e89ba7ed6aa69cbcd8eb39a38e8bb6d25e9a9700b7d66eacacb9aee17e89e782d7d24fa5aa8daed7218ab6adb3bb4a978a8e97f021b5a797b6b737e2a3''',
        'User-Agent': '''Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3829.0 Mobile Safari/537.36'''
    }
    html = requests.get(playListUrl,headers = headers).text
    playListName = re.findall("<title>(.*?) - 歌单 - 网易云音乐</title>", html)[0]
    print(f'已检测到歌单："{playListName}"，正在解析歌曲')
    songJson = re.findall('''window.REDUX_STATE = {"Playlist":{"data":(.*?),"info":{"id"''', html)[0]
    
    songs = json.loads(songJson)
    for song in songs:
        downLoad(song["id"])
        time.sleep(1)
    
    
    

if __name__ == "__main__":
    print("此程序无法下载已下架和付费歌曲！")
    print("所下载歌曲版权归网易所有，请勿用于商业用途，否则后果自负！")
    print("软件代码受 MIT 协议保护，严禁侵犯！https://github.com/FutureYu/NetEaseMusic")
    print('''
 _   _      _   _____                ___  ___          _      
| \ | |    | | |  ___|               |  \/  |         (_)     
|  \| | ___| |_| |__  __ _ ___  ___  | .  . |_   _ ___ _  ___ 
| . ` |/ _ \ __|  __|/ _` / __|/ _ \ | |\/| | | | / __| |/ __|
| |\  |  __/ |_| |__| (_| \__ \  __/ | |  | | |_| \__ \ | (__ 
\_| \_/\___|\__\____/\__,_|___/\___| \_|  |_/\__,_|___/_|\___|
''')
    print()

    while True:
        oldUrl = input("请复制网易云歌曲或歌单地址\n地址：") #https://music.163.com/#/song?id=228252
        print()

        if "playlist" in oldUrl:
            if "&" in oldUrl:
                playLists = re.findall("id=(.*[0-9])&",oldUrl)
            else:
                playLists = re.findall("id=(.*[0-9])",oldUrl)
            getSongs(playLists[0])
        elif "song" in oldUrl:
            if "&" in oldUrl:
                songIds = re.findall("id=(.*[0-9])&",oldUrl)
            else:
                songIds = re.findall("id=(.*[0-9])",oldUrl)
            downLoad(songIds[0])
        else:
            print("地址有误！")