from django.shortcuts import render
from django.http import HttpResponse
from .models import Consulta  # Importa o modelo Consulta
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import NameForm


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect("/thanks/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, "name.html", {"form": form})

# meuapp/views.py
def thanks(request):
    return render(request, 'thanks.html')

def home(request):
    if request.method == 'GET': # Verifica se o metodo é GET
        # Renderiza o template HTML
        return render(request, 'meuapp.html')
    elif request.method == 'POST':  # Verifica se o metodo é POST
        cnpj = request.POST.get('cnpj')  # Obtém o valor do campo 'cnpj' do formulário
        razao_social = request.POST.get('razao_social')

        consulta = Consulta(cnpj=cnpj, razao_social=razao_social)
        if Consulta.objects.filter(cnpj=cnpj).exists():
            return render(request, 'meuapp.html', {'success':"CNPJ já cadastrado!"})  # Retorna erro se o CNPJ já existe

        print(f"CNPJ: {cnpj}, Razão Social: {razao_social}")  # Imprime os valores no console
        return render(request, 'meuapp.html', {'error':"CNPJ não encontrado!"})  # Retorna sucesso se o CNPJ não existe
    return None