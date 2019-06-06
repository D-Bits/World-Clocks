from django.shortcuts import render
from django.views.generic import ListView
from . models import Africa, Asia


# View for Index page
def index(request):

    template_name = 'clocks/index.html'
    

# Show all African times in template
class AfricanTimesView(ListView):

    model = 'Africa'
    template_name = 'clocks/africa.html'