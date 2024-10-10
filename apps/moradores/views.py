from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import Morador

@login_required
def moradores(request):

    moradores = Morador.objects.order_by()
    
    context = {
        'nome_pagina' : 'Moradores',
        'moradores': moradores,
    }
    
    return render(request,'moradores.html', context)