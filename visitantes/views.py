from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from visitantes.forms import AutorizaVisitanteForm, VisitanteForm
from .models import Visitante

@login_required
def registrar_visitante(request):
    form = VisitanteForm()
    
    if request.method == 'POST':
        form = VisitanteForm(request.POST)
        
        if form.is_valid():
            visitante = form.save(commit=False)
            
            visitante.registrado_por = request.user.porteiro
            visitante = form.save()
            
            messages.success(request,'Visitante registrado com sucesso')
            return redirect('index')
        
    context ={
        'nome_pagina': 'Registrar visitante',
        'form': form
    }
    
    return render(request,'registrar_visitante.html',context)

@login_required
def informacoes_visitante(request, pk):
    
    visitante = get_object_or_404(Visitante,pk=pk)
    
    context ={
        'nome_pagina': 'Informações Visitante',
        'visitante': visitante
    }
    
    return render(request,'informacoes_visitante.html',context)