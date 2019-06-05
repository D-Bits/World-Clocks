from django.db import models
from pytz import timezone
from datetime import datetime

# Create your models here.

# Model for African timezones
class Africa(models.Model):

    # Time for Johannesburg, S. Africa
    joburg = timezone('Africa/Johannesburg')
    joburg_time = datetime.now(joburg)

    # Time for Nairobi, Kenya
    nairobi = timezone('Africa/Nairobi')
    nairobi_time = datetime.now(nairobi)

    # Time for Tripoli, Libya
    tripoli = timezone('Africa/Tripoli')
    tripoli_time = datetime.now(tripoli)

    # Time for Lagos, Nigeria
    lagos = timezone('Africa/Lagos')
    lagos_time = datetime.now(lagos)

    # Time for Kinshasa, D.R. Congo
    kinshasa = timezone('Africa/Kinshasa')
    lagos_time = datetime.now(kinshasa)

    # Time for Dakar, Senegal
    dakar = timezone('Africa/Senegal')
    dakar_time = datetime.now(dakar)

    # Time for Cairo, Egypt
    cairo = timezone('Africa/Cairo')
    cairo_time = datetime.now(cairo)