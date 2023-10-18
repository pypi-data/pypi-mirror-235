'''
动漫网站各种api
'''
from datetime import datetime
import requests
from lxml import etree


class AGE:
    '''
    AGE动漫网站
    '''
    def __init__(self):
        self.url = 'https://www.agemys.org/'
        self.__hot_url__ = 'https://www.agemys.org/rank?year='

    def get_current_week_hot(self,) -> list:
        '''
        return:返回 所在周top热番
        '''
        week_url = self.__hot_url__ + f'{datetime.now().year}'
        html = requests.get( week_url,timeout = 10 )
        if html.status_code == 200:
            week_name = etree.HTML(html.text).xpath('//div/div/div[1]/div[1]/div/div[2]//text()')
            week_hot = etree.HTML(html.text).xpath('//div/div/div[1]/div[1]/div/div[3]//text()')
            return {
                'name':week_name,
                'hot':week_hot
            }
        else:
            return {
                'msg': '获取信息失败'
            }

    def get_current_month_hot(self,) -> dict:
        '''
        return:返回 所在月份 top热番
        '''
        month_url = self.__hot_url__ + f'{datetime.now().year}'
        html = requests.get( month_url,timeout = 10 )
        if html.status_code == 200:
            month_name = etree.HTML(html.text).xpath('//div/div/div[1]/div[1]/div/div[2]//text()')
            month_hot = etree.HTML(html.text).xpath('//div/div/div[1]/div[1]/div/div[3]//text()')
            return  {
                'name':month_name,
                'hot':month_hot
            }
        else:
            return {
                'msg': '获取信息失败'
            }    
    def get_current_year_hot(self,) -> dict:
        '''
        return:返回 所在年份 top热番
        '''
        year_url = self.__hot_url__ + f'{datetime.now().year}'
        html = requests.get( year_url,timeout = 10 )
        if html.status_code == 200:
            year_name = etree.HTML(html.text).xpath('//div/div/div[1]/div[1]/div/div[2]//text()')
            year_hot = etree.HTML(html.text).xpath('//div/div/div[1]/div[1]/div/div[3]//text()')
            return {
                'name':year_name,
                'hot':year_hot
            }
        else:
            return {
                'msg': '获取信息失败'
            }

    def get_current_hot(self,) -> dict:
        '''
        return:返回 所在周、月、年 top热番
        '''
        week_url = self.__hot_url__ + f'{datetime.now().year}'
        html = requests.get( week_url,timeout = 10 )
        if html.status_code == 200:
            week_name = etree.HTML(html.text).xpath('//div/div/div[1]/div[1]/div/div[2]//text()')
            week_hot = etree.HTML(html.text).xpath('//div/div/div[1]/div[1]/div/div[3]//text()')
            month_name = etree.HTML(html.text).xpath('//div/div/div[1]/div[2]/div/div[2]//text()')
            month_hot = etree.HTML(html.text).xpath('//div/div/div[1]/div[2]/div/div[3]//text()')
            year_name = etree.HTML(html.text).xpath('//div/div/div[1]/div[3]/div/div[2]//text()')
            year_hot = etree.HTML(html.text).xpath('//div/div/div[1]/div[3]/div/div[3]//text()')
            return {
                'week':{
                    'name':week_name,
                    'hot':week_hot
                },
                'month':{
                    'name':month_name,
                    'hot':month_hot                    
                },
                'year':{
                    'name':year_name,
                    'hot':year_hot         
                }
            }
        else:
            return {
                'msg': '获取信息失败'
            }

