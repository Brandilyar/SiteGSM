from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,HttpResponseForbidden
from django.shortcuts import redirect
from django.views.generic import View
import datetime
from .models import Card
from .forms import PostForm
from report_gsm.transaction import *

class Get_report(View):
    def get(self,request):
        form = PostForm()
        context = {'form':form}
        return render (request, 'report_gsm/report_form.html',context=context)
    def post(self,request):
        form = PostForm(request.POST)
        data = form.__dict__
        number_card = data['data']['number_card']
        DateFrom = datetime.datetime.strptime(data['data']['DateFrom'],'%Y-%m-%d').strftime('%d.%m.%Y')
        DateTo = datetime.datetime.strptime(data['data']['DateTo'],'%Y-%m-%d').strftime('%d.%m.%Y')
        ready_data = get_transaction.get_transaction(number_card,DateFrom,DateTo)
        context = {'data_head':ready_data[0],'data_content':ready_data[1:]}
        return render (request, 'report_gsm/result.html',context=context)


    

    


