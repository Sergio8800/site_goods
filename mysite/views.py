from django.shortcuts import redirect

def redirect_list(request):
    return redirect('goods_list_url', permanent=True)