from django.shortcuts import render
from django.views.generic import ListView
from . models import Africa, Asia
from . times import africa, asia, n_america


# View for Index page
def index(request):

    template_name = 'clocks/index.html'

    return render(request, template_name)
    

# Show all African times in template
class AfricaList(ListView):

    model = Africa
    template_name = 'clocks/africa.html'