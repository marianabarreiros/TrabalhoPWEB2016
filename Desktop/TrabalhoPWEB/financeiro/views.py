from django.shortcuts import render

# Create your views here.
def sistema_financeiro(request):
    return render(request, 'financeiro/sistema_financeiro.html', {})