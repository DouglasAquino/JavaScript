from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import Noticia

def noticia_resumo_template(request):
    total = Noticia.objects.count()
    return render(request, 'app_noticias/resumo.html', {'total':total})


def noticia_detalhe(request, noticia_id):
    if request.user.is_superuser:
        try:
            noticia = Noticia.objects.get(pk=noticia_id)
            return render(request, 'app_noticias/detalhe.html', {'noticia':noticia})
        except Exception:
            raise Http404('Página não encontada')
        
        return render(request, 'app_noticias/detalhe.html', {'noticia':noticia})
    
    else:
        return HttpResponse('Voce não esta autorizado. <a href="/conta/login">Faça Login </a>')

def pagina_inicial(request):
    noticias = Noticia.objects.all()
    return render(request, 'app_noticias/inicial.html', {'todas_noticias':noticias})


