import datetime
import sys
import time

from analyze.models import RequestRecord
from django.utils import timezone
from django.views.debug import technical_500_response

from utils.utils import getRealIp, getLocation, parse_user_agent


class RequestRecordMiddleware():
    """
    把客户端信息记录到数据库便于统计分析
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip_addr = getRealIp(request)
        location = getLocation(ip_addr)
        if location == '':
            location = '局域网'
        platform_info = parse_user_agent(request)[1]
        browser_info = parse_user_agent(request)[2]

        r = RequestRecord.objects.filter(ip=ip_addr).filter(location=location).filter(os_info=platform_info) \
            .filter(browser=browser_info).first()
        if not r or (datetime.datetime.now() - r.access_time).total_seconds() > 3600:
            RequestRecord.objects.create(
                ip=ip_addr,
                location=location,
                os_info=platform_info,
                browser=browser_info
            )
        response = self.get_response(request)
        return response

    def process_exception(self, reqeust, exception):
        if reqeust.user.is_superuser:
            return technical_500_response(reqeust, *sys.exc_info())
