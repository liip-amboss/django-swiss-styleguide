from django.conf import settings


def swiss_styleguide(request):
    return {
        'app_title': settings.SWISS_STYLEGUIDE['app_title'],
        'department_title':  settings.SWISS_STYLEGUIDE['department_title'],
        'available_languages': dict(settings.LANGUAGES).keys()
    }
