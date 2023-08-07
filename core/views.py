from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import ParticipanteForm
from django.contrib import messages



def obrigado(request):
    return render(request, 'core/obrigado.html')


def home(request):
    if request.method == 'POST':
        form = ParticipanteForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('core:redirect-cad')
            return redirect('core:obrigado')
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
    else:
        form = ParticipanteForm()

    return render(request, 'core/index.html', {'form': form})

def redirect_cadastro(request):
    return render(request, 'core/redirect-cad.html')



