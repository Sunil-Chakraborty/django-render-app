from django.http import HttpResponse
from .models import Report

def reports(request):
    data = Report.objects.all()
    output = ", ".join([r.title for r in data])
    return HttpResponse(output)