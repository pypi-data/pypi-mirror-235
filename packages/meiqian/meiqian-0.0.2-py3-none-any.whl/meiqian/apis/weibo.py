'''
微博相关榜单数据
'''
import time
import datetime
from urllib.parse import urlencode


import re
import requests

class WEIBO:
    '''
    微博榜单数据
    '''
    def hot_topic(self,page:int=1,count:int=10,timeout:int=10) -> dict:
        '''
        page:当前页码,范围为1到10
        count:每页数量,建议值为10
        return:返回实时话题排行榜数据
        '''
        url = 'https://weibo.com/ajax/statuses/topic_band'
        data = {
            'sid':'v_weibopro',
            'category':'all',
            'page':page,
            'count':count
        }
        html = requests.get(url,params=data,timeout=timeout)
        if html.status_code == 200:
            return html.json()
        return {'msg':'获取信息失败'}

    def hot_search(self,timeout:int=10) -> dict:
        '''
        return:实时热搜排行榜数据
        '''
        url = 'https://weibo.com/ajax/side/hotSearch'
        return self.__get_data(url=url,cookie=False,timeout=timeout)

    def hot_entertainment(self,timeout:int=10) -> dict:
        '''
        timeout:请求时长
        return:实时文娱排行榜数据
        '''
        url = 'https://weibo.com/ajax/statuses/entertainment'
        return self.__get_data(url=url,cookie=True,timeout=timeout)

    def hot_news(self,timeout:int=10) -> dict:
        '''
        timeout:请求时长
        return:社会新闻排行榜
        '''
        url = 'https://weibo.com/ajax/statuses/news'
        return self.__get_data(url=url,cookie=True,timeout=timeout)


    def hot_movies_of_day_show(self,timeout:int=10)->dict:
        '''
        return:获取微博已上映电影每日榜单
        '''
        return self.__get_movie_data(movie_type='day',show=True,timeout=timeout)

    def hot_movies_of_week_show(self,timeout:int=10)->dict:
        '''
        return:获取微博已上映电影每周榜单
        '''
        return self.__get_movie_data(movie_type='week',show=True,timeout=timeout)

    def hot_movies_of_day_unshow(self,timeout:int=10)->dict:
        '''
        return:获取微博未上映电影每日榜单
        '''
        return self.__get_movie_data(movie_type='day',show=False,timeout=timeout)

    def hot_movies_of_week_unshow(self,timeout:int=10)->dict:
        '''
        return:获取微博未上映电影每周榜单
        '''
        return self.__get_movie_data(movie_type='week',show=False,timeout=timeout) 

    def __get_movie_data(self,movie_type='day',show=True,timeout:int=10)->dict:
        '''
        获取电影相关信息
        '''
        url = 'https://movie.weibo.com/movie/webajax/newrank'
        headers = {
            'Referer':'https://movie.weibo.com/'
        }
        today = datetime.date.today()
        if movie_type == 'day':
            yesterday = (today - datetime.timedelta(days=1)).strftime('%Y/%m/%d')
            if show:
                data = {
                    'type': 'hotshowday',
                    'date': yesterday
                }
            else:
                data = {
                    'type': 'unshowday',
                    'date': yesterday
                }
        else:
            last_sunday = today - datetime.timedelta(days=today.weekday() + 1)
            if show:
                data = {
                    'type': 'hotshowweek',
                    'date': last_sunday
                }
            else:
                data = {
                    'type': 'unshowweek',
                    'date': last_sunday
                }
        html = requests.get(
            url,
            params = data,
            timeout=timeout,
            allow_redirects=False,
            headers = headers
        )
        if html.status_code == 200:
            return html.json()
        return {'msg':'获取信息失败'}

    # 数据获取
    def __get_data(self,url,cookie=False,timeout=10,) ->dict:
        '''
        内部调用
        '''
        headers = {}
        if cookie:
            cookie = self.__generator_cookie(url)
            headers = {
                'Cookie': cookie
            }
        html = requests.get(
            url,
            timeout=timeout,
            allow_redirects=False,
            headers = headers
        )
        if html.status_code == 200:
            return html.json()
        return {'msg':'获取信息失败'}

    def __generator_cookie(self,url,timeout=10):
        '''
        用于产生临时cookie
        '''
        token = requests.get(
            url,
            allow_redirects=False,
            timeout=timeout
        )
        finally_cookie  = token.headers['set-cookie'].split(';')[0]+';'
        referer_data = {
            'entry': 'miniblog',
            'a': 'enter',
            'url': 'https://weibo.com/ajax/statuses/entertainment',
            'domain': 'weibo.com',
            'ua': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
            '_rand':int(time.time()*1000)
        }
        referer1 = 'https://passport.weibo.com/visitor/visitor?' + urlencode(referer_data)
        url1 = 'https://passport.weibo.com/visitor/genvisitor'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
            'Referer': referer1 
        }
        browser_info = "cb=gen_callback&fp=%7B%22os%22%3A%221%22%2C%22browser%22%3A%22Chrome118%2C0%2C0%2C0%22%2C%22fonts%22%3A%22undefined%22%2C%22screenInfo%22%3A%221920*1080*24%22%2C%22plugins%22%3A%22Portable%20Document%20Format%3A%3Ainternal-pdf-viewer%3A%3APDF%20Viewer%7CPortable%20Document%20Format%3A%3Ainternal-pdf-viewer%3A%3AChrome%20PDF%20Viewer%7CPortable%20Document%20Format%3A%3Ainternal-pdf-viewer%3A%3AChromium%20PDF%20Viewer%7CPortable%20Document%20Format%3A%3Ainternal-pdf-viewer%3A%3AMicrosoft%20Edge%20PDF%20Viewer%7CPortable%20Document%20Format%3A%3Ainternal-pdf-viewer%3A%3AWebKit%20built-in%20PDF%22%7D"
        false  = 'false'
        true = 'true'
        tid_infos = requests.post(
            url1,
            headers=headers,
            data=browser_info,
            timeout=timeout
        ).text
        tid = eval(
            re.findall(
                '"data":({.*?})',
                tid_infos
            )[0]
        )['tid']
        params = {
            'a': 'incarnate',
            't': tid, # tid参数
            'w': '2',
            'c': '095',
            'gc': '',
            'cb': 'cross_domain',
            'from': 'weibo',
            '_rand': '0.4839562921396081'
        }
        urlss = 'https://passport.weibo.com/visitor/visitor?' + urlencode(params)
        add_cookies_info = requests.get(urlss,timeout=timeout).text
        add_cookies = eval(
            re.findall(
                '"data":({.*?})',
                add_cookies_info
            )[0] )
        for a,b in add_cookies.items():
            finally_cookie = finally_cookie  + a.upper() +'=' + b+';'
        return finally_cookie[:-1]
