from datetime import datetime

def current_datetime(request):
    return {
        'date_time': datetime.now()
    }