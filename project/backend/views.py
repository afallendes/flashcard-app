from django.http import JsonResponse

def hello_world(request):
    return JsonResponse({'status': 'OK', 'message': 'Hello World!'}, status=200)
