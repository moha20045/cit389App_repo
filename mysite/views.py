from django.http import HttpResponse

def home(request):
    return HttpResponse("""
    Hello from Elastic Beanstalk Django App!<br>
    Mohamed Maidan Hello from Elastic Beanstalk django App!<br>
    Atlantis university Hello from Elastic Beanstalk Django App!
    """)