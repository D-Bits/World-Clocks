from django.db import models
from pytz import timezone
from datetime import datetime

# Create your models here.

# Model for African timezones/cites
class Africa():

    # Cairo, Egypt time
    cairo = timezone('Africa/Cairo')
    cairo_time = datetime.now(cairo)

    # Johanesburg, S. Africa time
    joburg = timezone('Africa/Johannesburg')
    joburg_time = datetime.now(joburg)

    # Lagos, Nigeria time
    lagos = timezone('Africa/Lagos')
    lagos_time = datetime.now(lagos)

    # Kinshasa, D.R. Congo time
    kinshasa = timezone('Africa/Kinshasa')
    kinshasa_time = datetime.now(kinshasa)

    # Nairobi, Kenya time
    nairobi = timezone('Africa/Nairobi')
    nairobi_time = datetime.now(nairobi)

    # Tripoli, Libya time
    tripoli = timezone('Africa/Tripoli')
    tripoli_time = datetime.now(tripoli)


# Asian Timezones
class Asia(models.Model):

    # Time for Tokyo, Japan
    tokyo = timezone('Asia/Tokyo')
    tokyo_time = datetime.now(tokyo)

    # Time for Seoul, SK
    seoul = timezone('Asia/Seoul')
    seoul_time = datetime.now(seoul)

    # Time for Delhi, India
    delhi = timezone('Asia/Bishkek')
    delhi_time = datetime.now(delhi)

    # Time for Beijing, China
    beijing = timezone('Asia/Beijing')
    beijing_time = datetime.now(beijing)

    # Time for Shanghai, China
    shanghai = timezone('Asia/Shanghai')
    shanghai_time = datetime.now(shanghai)

    # Time for Hong Kong, China
    hong_kong = timezone('Asia/Hong_Kong')
    hong_kong_time = datetime.now(hong_kong)

    # Time for Singapore
    

    # Time for Bangkok, Thailand

    # Time for Tashket, Uzbekistan

    # Time for Ulan Bator, Mongolia
