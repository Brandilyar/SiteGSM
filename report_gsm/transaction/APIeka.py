from zeep import Client
from datetime import datetime, date, time
import os
https_proxy = 'http://proxy.ozon.ru:3128'
os.environ["HTTPS_PROXY"] = https_proxy
os.environ["HTTP_PROXY"] = https_proxy
login = 'OZON'
password = 'Fleet2020'
def AddCardNomenclature_(curdNumbe,nomenclatureCode):   # Добавление номенклатуры карты
	client = Client('https://apizenda.eka.ru/WebApiEkaPro.asmx?WSDL')
	result = client.service.AddCardNomenclature(login,password,curdNumbe,nomenclatureCode)
	return result
def AddLimitOnCard_(curdNumbe,nomenclatureCode,periodTypeId,unitId,value):  # Добавление лимита карты
	client = Client('https://apizenda.eka.ru/WebApiEkaPro.asmx?WSDL')
	result = client.service.AddLimitOnCard(login,password,curdNumbe,nomenclatureCode,periodTypeId,unitId,value)
	return result
def BlockCard_(curdNumbe):  # Блокировка карты
	client = Client('https://apizenda.eka.ru/WebApiEkaPro.asmx?WSDL')
	result = client.service.BlockCard(login,password,curdNumbe)
	return result
def ChangeLimitOfCard_(curdNumbe,nomenclature,periodTypeId,newValue):  # Изменение существующего лимита
	client = Client('https://apizenda.eka.ru/WebApiEkaPro.asmx?WSDL')
	result = client.service.ChangeLimitOfCard(login,password,curdNumbe,nomenclature,periodTypeId,newValue)
	return result
def GetAcountsCards_(accountNumber):  # Получение списка карт по счету
	client = Client('https://apizenda.eka.ru/WebApiEkaPro.asmx?WSDL')
	result = client.service.GetAcountsCards(login,password,accountNumber)
	return result			
def GetCardNomenclature_(curdNumbe): # Получить номенклатуры карты
	client = Client('https://apizenda.eka.ru/WebApiEkaPro.asmx?WSDL')
	result = client.service.GetCardNomenclature(login,password,curdNumbe)
	return result
def GetCurrentBalance_(accountNumber): # Получить баланс счета
	client = Client('https://apizenda.eka.ru/WebApiEkaPro.asmx?WSDL')
	result = client.service.GetCurrentBalance(login,password,accountNumber)
	return result
def GetEkaRRN_(externalRRN): # Получить внутренний RRN транзакции.
	client = Client('https://apizenda.eka.ru/WebApiEkaPro.asmx?WSDL')
	result = client.service.GetEkaRRN(login,password,externalRRN)
	return result
def GetExternalRRN_(ekaRRN): # Получить внешний RRN транзакции.
	client = Client('https://apizenda.eka.ru/WebApiEkaPro.asmx?WSDL')
	result = client.service.GetExternalRRN(login,password,ekaRRN)
	return result
def GetLimitsOfCard_(curdNumbe):  # Получение лимита карты
	client = Client('https://apizenda.eka.ru/WebApiEkaPro.asmx?WSDL')
	result = client.service.GetLimitsOfCard(login,password,curdNumbe)
	return result
def GetLimitsOfCards_(accountNumber):  # Метод получения лимитов по всем картам доступным пользователю.
	client = Client('https://apizenda.eka.ru/WebApiEkaPro.asmx?WSDL')
	result = client.service.GetLimitsOfCards(login,password,accountNumber)
	return result
def GetTerminalLocations_():  # Метод получения списка установленных терминалов.
	client = Client('https://apizenda.eka.ru/WebApiEkaPro.asmx?WSDL')
	result = client.service.GetTerminalLocations(login,password)
	return result
def GetTransactions_(dateFrom,dateTo):  # Метод возвращает транзакции с авторизацией и начисленными компенсациями.
	transactiondogovor={}
	client = Client('https://apizenda.eka.ru/WebApiEkaPro.asmx?WSDL')
	result_CB_0002077 = client.service.GetTransactions(login,password,'СВ-0002077',datetime.strptime(dateFrom,"%d.%m.%Y"),datetime.strptime(dateTo,"%d.%m.%Y"))
	result_CB_0002111 = client.service.GetTransactions(login,password,'СВ-0002111',datetime.strptime(dateFrom,"%d.%m.%Y"),datetime.strptime(dateTo,"%d.%m.%Y"))
	transactiondogovor = {'СВ-0002077':result_CB_0002077,'СВ-0002111':result_CB_0002111}
	return transactiondogovor
def GetUnconfirmedTransactions_():  # Метод возвращает все предавторизации за последние 12 часов.
	client = Client('https://apizenda.eka.ru/WebApiEkaPro.asmx?WSDL')
	result_CB_0002077 = client.service.GetUnconfirmedTransactions(login,password,'СВ-0002077')
	result_CB_0002111 = client.service.GetUnconfirmedTransactions(login,password,'СВ-0002111')
	return result_CB_0002077,result_CB_0002111
def RemoveCardLimit_(curdNumbe,nomenclatureCode,periodTypeId): # Удаление лимита карты
	client = Client('https://apizenda.eka.ru/WebApiEkaPro.asmx?WSDL')
	result = client.service.RemoveCardLimit(login,password,curdNumbe,nomenclatureCode,periodTypeId)
	return result
def RemoveCardNomenclature_(curdNumbe,nomenclatureCode):  # Удаление номенклатуры карты
	client = Client('https://apizenda.eka.ru/WebApiEkaPro.asmx?WSDL')
	result = client.service.RemoveCardNomenclature(login,password,curdNumbe,nomenclatureCode)
	return result
def UnblockCard_(curdNumbe):  # Разблокировка карты
	client = Client('https://apizenda.eka.ru/WebApiEkaPro.asmx?WSDL')
	result = client.service.UnblockCard(login,password,curdNumbe)
	return result
def GetCardTransactions_(curdNumbe,dateFrom,dateTo):  # Транзакции одной карты
	client = Client('https://apizenda.eka.ru/WebApiEkaPro.asmx?WSDL')
	result = client.service.GetCardTransactions(login,password,curdNumbe,datetime.strptime(dateFrom,"%d.%m.%Y"),datetime.strptime(dateTo,"%d.%m.%Y"))
	return result
def GetLimitsOfCardsOneCard_():  # Метод получения лимитов по всем картам доступным пользователю.
	client = Client('https://apizenda.eka.ru/WebApiEkaPro.asmx?WSDL')
	result_CB_0002077 = client.service.GetLimitsOfCards(login,password,'СВ-0002077')
	result_CB_0002111 = client.service.GetLimitsOfCards(login,password,'СВ-0002111')
	return result_CB_0002077,result_CB_0002111
def ChangeNom(curdNumbe,nomenclatureCode,periodTypeId,unitId,value): # Изменение лимита карты с изменением номенклатуры
	while GetCardInfo_(curdNumbe)['Info']['Enabled'] == False:
		UnblockCard_(curdNumbe)
	for i in range(len(GetCardNomenclature_(curdNumbe)['Items']['CardNomenclatureItem'])):
		if GetCardNomenclature_(curdNumbe)['Items']['CardNomenclatureItem'][i]['NomenclatureCode'] == nomenclatureCode:
			if GetLimitsOfCard_(curdNumbe)['Items'] == None:					
				AddLimitOnCard_(curdNumbe,nomenclatureCode,periodTypeId,unitId,value)
			else:
				ChangeLimitOfCard_(curdNumbe,nomenclatureCode,periodTypeId,value)
		else:
			RemoveCardNomenclature_(curdNumbe,GetCardNomenclature_(curdNumbe)['Items']['CardNomenclatureItem'][i]['NomenclatureCode'])	
	if GetCardNomenclature_(curdNumbe)['Items'] == None:
		AddCardNomenclature_(curdNumbe,nomenclatureCode)
		while GetLimitsOfCard_(curdNumbe)['Items'] == None:
			AddLimitOnCard_(curdNumbe,nomenclatureCode,periodTypeId,unitId,value)
def GetCardInfo_(curdNumbe): # Метод возвращает информацию по топливной карте
	client = Client('https://apizenda.eka.ru/WebApiEkaPro.asmx?WSDL')
	result = client.service.GetCardInfo(login,password,curdNumbe)
	return result	