import time

from django.utils.deprecation import MiddlewareMixin

from analyze.models import RequestRecord
from utils.utils import getRealIp, getLocation, parse_user_agent


class RequestRecordMiddleware(MiddlewareMixin):
    """
    把客户端信息记录到数据库便于统计分析
    """

    def process_reqeust(self, request):
        ip_addr = getRealIp(request)
        location = getLocation(request)
        if location == '':
            location = '局域网'
        platform_info = parse_user_agent(request)[1]
        browser_info = parse_user_agent(request)[2]

        r = RequestRecord.objects.filter(ip=ip_addr).filter(location=location).filter(os_info=platform_info) \
            .filter(browser=browser_info).first()
        if not r or time.time() - r.access.time > 3600:
            RequestRecord.objects.create(
                ip=ip_addr,
                location=location,
                os_info=platform_info,
                browser=browser_info
            )
