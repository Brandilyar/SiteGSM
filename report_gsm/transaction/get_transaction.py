from .APIeka import GetCardTransactions_
import datetime

def get_transaction(curdNumbe,dateFrom,dateTo):
    # Получение транзакции для карты за период
    transaction=GetCardTransactions_(curdNumbe,dateFrom,dateTo)
    common_list_transaction = []
    # Заголовки
    head_list = ['Дата операции','Номер карты','Услуга','Количество','Цена','Сумма','Скидка','Сумма со скидкой','Владелец','Номер ТО','Номер терминала']
    common_list_transaction.append(head_list)
    # Перебор списка транзакций
    for one_transaction in transaction['Items']['TransItem']:
        list_one_transaction = [one_transaction['TransactionDate'].strftime('%d.%m.%Y')+' '+one_transaction['TransactionTime'],
                                one_transaction['CardNumber'],
                                one_transaction['Nomenclature'],
                                one_transaction['Quantity'],
                                one_transaction['Price'],
                                one_transaction['Amount'],
                                one_transaction['Amount']-one_transaction['Quantity']*one_transaction['TotalPrice'],
                                one_transaction['Quantity']*one_transaction['TotalPrice'],
                                one_transaction['MerchantOwner'],
                                one_transaction['MerchantAddress'],
                                one_transaction['TerminalCode']
                                ]
        common_list_transaction.append(list_one_transaction)
    return common_list_transaction

