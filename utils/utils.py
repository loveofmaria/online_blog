import os

import geoip2.database
import geoip2.errors
from user_agents import parse

cities = ['北京', '上海', '天津', '重庆']

file_path = os.path.abspath(os.path.dirname(__file__))


def get_database_setting(env):
    """
    根据不同的配置设置数据库配置
    """
    database = {
        'host': '',
        'name': '',
        'user': '',
        'password': '',
    }
    if env == 'development':
        database['host'] = os.getenv('IZONE_MYSQL_HOST_LOCAL')
        database['name'] = os.getenv('IZONE_MYSQL_NAME_LOCAL')
        database['user'] = os.getenv('IZONE_MYSQL_USER_LOCAL')
        database['password'] = os.getenv('IZONE_MYSQL_PASSWORD_LOCAL')
    elif env == 'production':
        database['host'] = os.getenv('IZONE_MYSQL_HOST')
        database['name'] = os.getenv('IZONE_MYSQL_NAME')
        database['user'] = os.getenv('IZONE_MYSQL_USER')
        database['password'] = os.getenv('IZONE_MYSQL_PASSWORD')
    return database


def getLocation(ip):
    """
    根据参数IP地址，获取访问的区域
    如果无效，则返回空字符串
    """
    location = ''
    try:
        reader = geoip2.database.Reader(os.path.join(file_path, 'GeoLite2-City.mmdb'))
        res = reader.city(ip)
        try:
            subdivisions = res.subdivisions.most_specific.names['zh-CN']
        except KeyError:
            subdivisions = ''
        country = res.country.names['zh-CN']
        try:
            city = res.city.names['zh-CN']
            if city in cities:
                city = ''
        except KeyError:
            city = ''
        if country == city:
            location = country
        else:
            location = country + subdivisions + city
    except geoip2.errors.AddressNotFoundError:
        pass
    return location


def getRealIp(request):
    ip = request.META['REMOTE_ADDR']
    if 'HTTP_X_FORWARDED_FOR' in request.META:
        ip = request.META['HTTP_X_FORWARDED_FOR']
    return ip


def parse_user_agent(request):
    user_agent_str = request.META.get('HTTP_USER_AGENT', 'unknown')
    user_agent = parse(user_agent_str)
    return str(user_agent).split('/')


def isEmoji(content):
    """
    判断内容是否是emoji
    """
    if not content:
        return False
    if u"\U0001F600" <= content <= u"\U0001F64F":
        return True
    elif u"\U0001F300" <= content <= u"\U0001F5FF":
        return True
    elif u"\U0001F680" <= content <= u"\U0001F6FF":
        return True
    elif u"\U0001F1E0" <= content <= u"\U0001F1FF":
        return True
    else:
        return False
