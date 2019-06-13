from django.shortcuts import render
from django.views.generic import ListView
from . times import (africa, asia, europe, middle_east,
                     n_america, oceania, s_america
                    )


# View for Index page
def index(request):

    template_name = 'clocks/index.html'
    title = "Home "

    return render(request, template_name)
    

# View for African cities
def africa_times(request):

    template_name = 'clocks/africa.html'
    context = africa
    title = "Africa "

    return render(request, template_name, context=context)
