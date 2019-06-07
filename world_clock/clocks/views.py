from django.shortcuts import render
from django.views.generic import ListView
from . times import (africa, asia, europe, middle_east,
                     n_america, oceania, s_america
                    )


# View for Index page
def index(request):

    template_name = 'clocks/index.html'

    return render(request, template_name)
    

