from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def hello(request):
    """联调探针：返回固定的问候语与服务器时间。"""
    return Response(
        {
            "code": 0,
            "message": "Hello World",
            "data": {
                "service": "ad-platform-backend",
                "server_time": timezone.localtime().strftime("%Y-%m-%d %H:%M:%S"),
            },
        }
    )
