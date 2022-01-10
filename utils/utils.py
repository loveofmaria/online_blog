import os

import geoip2.database
import geoip2.errors
from user_agents import parse

from izone import settings


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
        reader = geoip2.database.Reader(settings.GEOIP_DATABASE_PATH)
        response = reader.city(ip)
        subdivisions = response.subdivisions.most_specific.names['zh-CN']
        city = response.city.names['zh-CN']
        location = subdivisions + city
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


def get_ip_addr_from_meta(request):
    if 'HTTP_X_FORWARDED_FOR' in request.META:
        ip_addr = request.META.get('HTTP_X_FORWARDED_FOR')
    else:
        ip_addr = request.META.get('REMOTE_ADDR')
    return ip_addr
