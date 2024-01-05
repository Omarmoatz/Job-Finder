from .models import Main
def info(request):
    data = Main.objects.last()
    return {'data':data}
