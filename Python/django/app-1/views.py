from django.http import HttpResponse
from datetime import datetime, date, time, timezone

def currentDT(request):
    now = datetime.now()
    now = f"{now.day}/{now.month}/{now.year} - {now.hour}:{now.minute}:{now.second}"
    html = '<html lang="en"><body>Today is %s.</body></html>' % now
    return HttpResponse(html)