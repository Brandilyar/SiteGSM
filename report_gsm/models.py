from django.db import models
from model_utils import Choices
import os
import json
def json_data():
	with open(os.path.dirname(__file__)+'/data.json','r',encoding='utf-8') as file:
		data = json.load(file)		
	return data
class Card(models.Model):
    '''Модель топливной карты'''
    data = json_data()
    number_card_choices = tuple(data['number_card'])
    number_card = models.CharField('Номер карты',max_length = 20,choices=Choices(*number_card_choices)) #Номер топливных карт
    pin = models.IntegerField('Пин-код',default=0000) # Пин-код карты
    nomenclature = models.ForeignKey("Nomenclature",null=True, on_delete=models.SET_NULL,verbose_name='Номенклатура') # Номенклатура карты
    limit_type = models.ForeignKey("LimitTipe",null=True, on_delete=models.SET_NULL,verbose_name='Тип лимита') # Тип лимита карты карты
    viev_limit = models.ForeignKey("VievLimit",null=True, on_delete=models.SET_NULL,verbose_name='Вид лимита') # Вид лимита карты
    limit = models.IntegerField('Лимит',default=0) # Пин-код карты
    holder = models.ForeignKey("Holder",null=True,blank=True, on_delete=models.SET_NULL,verbose_name='Держатель') #Держатель карты
    government_number = models.ForeignKey("Car",null=True, on_delete=models.SET_NULL,verbose_name='Государственный номер')

    class Meta:
        '''Изменение название представления'''
        verbose_name = 'Топливные карты'
        verbose_name_plural = 'Топливная карта'

class LimitTipe(models.Model):
    '''Модель типа лимита карты'''
    name_limit_type = models.CharField('Тип лимита',max_length=15) # Название типа лимита карты

    class Meta:
        '''Изменение название представления'''
        verbose_name = 'Тип лимита'
        verbose_name_plural = 'Типы лимитов'

    def __str__(self):
        return self.name_limit_type

class Nomenclature(models.Model):
    '''Модель номенклатуры карты'''
    name_nomenclature = models.CharField('Номенклатура',max_length=15) # Название номенклатуры карты

    class Meta:
        '''Изменение название представления'''
        verbose_name = 'Номенклатура'
        verbose_name_plural = 'Номенклатуры'

    def __str__(self):
        return self.name_nomenclature

class VievLimit(models.Model):
    '''Модель вида лимита топливной карты'''
    viev_limit = models.CharField('Вид лимита',max_length=15) # Навзвание вида лимита карты

    class Meta:
        '''Изменение название представления'''
        verbose_name = 'Вид лимита'
        verbose_name_plural = 'Виды лимитов'

    def __str__(self):
        return self.viev_limit

class Holder(models.Model):
    '''Модель держателя топливной карты'''
    holder = models.CharField('ФИО',max_length=40) # ФИО держателя
    personnel_number = models.CharField('Табельный номер',max_length=15) # Табельный номер

    class Meta:
        '''Изменение название представления'''
        verbose_name = 'Держатель'
        verbose_name_plural = 'Держатели'

    def __str__(self):
        ready_name = self.holder +' табельный номер '+ self.personnel_number
        return ready_name

class Car(models.Model):
    '''Модель транспортного средства'''
    government_number = models.CharField('Государтсвенный номер',max_length=10) # Государственный номер
    car_model = models.ForeignKey("CarModel",null=True, on_delete=models.SET_NULL,verbose_name='Модель')
    car_nomenclature = models.ForeignKey("Nomenclature",null=True, on_delete=models.SET_NULL,verbose_name='Номенклатура') # Номенклатура транспортного средства
    car_type = models.CharField('Тип ТС',max_length=30) # Тип ТС
    year_of_issue = models.CharField('Год', max_length=50,null = True, blank= True) # Год выпуска
    vin = models.CharField('Vin номер', max_length=50,null = True, blank= True) # Vin номер
    color = models.CharField('Цвет', max_length=50,null = True, blank= True) # Цвет транспортного средства
    power = models.CharField('Мощность', max_length=50,null = True, blank= True) # Мощность транспортного средства

    class Meta:
        '''Изменение название представления'''
        verbose_name = 'Транспортное средство'
        verbose_name_plural = 'Транспортные средства'

    def __str__(self):
        return self.government_number


class CarModel(models.Model):
    name_model = models.CharField('Модель ТС',max_length=30) # Модель транспортного средства

    class Meta:
        '''Изменение название представления'''
        verbose_name = 'Модель'
        verbose_name_plural = 'Модели'

    def __str__(self):
        return self.name_model

class Column(models.Model):
    name_column = models.CharField('Колонна',max_length=30) # Название колонны
    class Meta:
        '''Изменение название представления'''
        verbose_name = 'Колонна'
        verbose_name_plural = 'Колонны'
    def __str__(self):
        return self.name_column
