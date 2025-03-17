from django.http import HttpResponse
from datetime import datetime, date, time, timezone

def DT(request):
    now = datetime.now()
    now = f"{now.day}/{now.month}/{now.year} - {now.hour}:{now.minute}:{now.second}"
    html = '''
    <html lang="en">
    <body>
    Hello, here we display the current date and time!<br><br>Reload the page to update the values below.<br><br>Today is %s.
    </body>
    </html>
    ''' % now
    return HttpResponse(html)