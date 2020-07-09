from django.contrib import admin
from .models import Card, LimitTipe, Nomenclature,VievLimit,Holder,Car,CarModel,Column

# Регистрация модели в админке
admin.site.register(Card)
admin.site.register(LimitTipe)
admin.site.register(Nomenclature)
admin.site.register(VievLimit)
admin.site.register(Holder)
admin.site.register(Car)
admin.site.register(CarModel)
admin.site.register(Column)

