from django.conf import settings


def auth(request):
    return {
        'app_title': settings.SWISS_STYLEGUIDE['app_title'],
        'department_title':  settings.SWISS_STYLEGUIDE['department_title']
    }
