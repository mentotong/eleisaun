from logging.config import IDENTIFIER
from django.shortcuts import render, redirect, get_object_or_404
from apuramentu.models import *
from django.db.models import Sum





def dashboard(request):
    sentru_votasaun_id = request.GET.get('fatin_vota')
    ronda = request.GET.get('volta_dahira')
    print('Ronda', ronda)
    context = get_context_data_for_timor_leste(sentru_votasaun_id, ronda)

    if ronda == '6':
        template_name = 'index-first.html'
    else:
        template_name = 'index.html'

    if not sentru_votasaun_id is None and not ronda is None:
        print('not none')
        if int(sentru_votasaun_id) <= 18:
            print('under 18')
            context = get_context_data(sentru_votasaun_id, ronda)
        elif int(sentru_votasaun_id) == 19:
            print('19')
            context = get_context_data_for_timor_leste(sentru_votasaun_id, ronda)
        elif int(sentru_votasaun_id) == 20:
            print('20')
            context = get_context_data_for_nivel('Natl', sentru_votasaun_id, ronda)
        else:
            print('21')
            context = get_context_data_for_nivel('Intl', sentru_votasaun_id, ronda)

    if request.htmx and (ronda=='6' or ronda is None):
        template_name = 'partials/first-election-chart.html'
        print('first round')
        return render(request, template_name, context)
        
    if request.htmx and (ronda=='7' or ronda is None):
        template_name = 'partials/second-election-chart.html'
        print('second round')
        return render(request, template_name, context)

    return render(request, template_name, context)



def get_context_data(id, ronda):
    print('data')
    print(ronda)
    dahira_label = ''
    apuramentu = ''
    somatoriu_votu = ''
    sentru_votasaun = "Timor-Leste"
    sentru_votasaun_hotu = SentruVotasaun.objects.all()
    jrh_total_votu = 50
    fgl_total_votu = 50
    jrh_persentajen = '50%'
    fgl_persentajen = '50%'
    
    sentru_votasaun = SentruVotasaun.objects.get(id=id)
    sentru_votasaun_hotu = SentruVotasaun.objects.all()

    if ronda == '6': 
        dahira_label = 'Volta Dahuluk (1)' 
        apuramentu = Apuramentu.objects.filter(sentru_votasaun=id, eleisaun=ronda).order_by('-total_votu')
        somatoriu_votu = Apuramentu.objects.filter(sentru_votasaun=id, eleisaun=ronda).aggregate(soma=Sum('total_votu'))['soma']
    else: 
        dahira_label = 'Volta Daruak (2)'
        jrh_total_votu = Apuramentu.objects.filter(eleisaun=ronda, sentru_votasaun=id, kandidatu='14').aggregate(total_votu_apuradu=Sum('total_votu'))['total_votu_apuradu']
        fgl_total_votu = Apuramentu.objects.filter(eleisaun=ronda, sentru_votasaun=id, kandidatu='6').aggregate(total_votu_apuradu=Sum('total_votu'))['total_votu_apuradu']
        try:
            jrh_persentajen = (jrh_total_votu/(jrh_total_votu+fgl_total_votu))*100
            fgl_persentajen = (fgl_total_votu/(jrh_total_votu+fgl_total_votu))*100
        except:
            jrh_total_votu = 1
            fgl_total_votu = 1
            jrh_persentajen = '0'
            fgl_persentajen = '0'

    context = {
        'apuramentu': apuramentu,
        'sentru_votasaun': sentru_votasaun,
        'somatoriu_votu': somatoriu_votu,
        'sentru_votasaun_hotu': sentru_votasaun_hotu,
        'sentru_id': id,
        'dahira_label': dahira_label,
        'jrh_total_votu': jrh_total_votu,
        'fgl_total_votu': fgl_total_votu,
        'jrh_persentajen': jrh_persentajen,
        'fgl_persentajen': fgl_persentajen,
        'ronda': ronda,
    }

    return context



def get_context_data_for_timor_leste(id, ronda):
    print('tl')
    dahira_label = ''
    apuramentu = ''
    somatoriu_votu = ''
    sentru_votasaun = "Timor-Leste"
    sentru_votasaun_hotu = SentruVotasaun.objects.all()
    jrh_total_votu = 50
    fgl_total_votu = 50
    jrh_persentajen = '50%'
    fgl_persentajen = '50%'


    if ronda == '6': 
        dahira_label = 'Volta Dahuluk (1)'
        apuramentu = Apuramentu.objects.filter(eleisaun=ronda).values('kandidatu').order_by('-total_votu').annotate(total_votu=Sum('total_votu'))
        somatoriu_votu = Apuramentu.objects.filter(eleisaun=ronda).aggregate(soma=Sum('total_votu'))['soma']
    else: 
        dahira_label = 'Volta Daruak (2)'
        jrh_total_votu = Apuramentu.objects.filter(eleisaun=ronda, kandidatu='14').aggregate(total_votu_apuradu=Sum('total_votu'))['total_votu_apuradu']
        fgl_total_votu = Apuramentu.objects.filter(eleisaun=ronda, kandidatu='6').aggregate(total_votu_apuradu=Sum('total_votu'))['total_votu_apuradu']
        try:
            jrh_persentajen = (jrh_total_votu/(jrh_total_votu+fgl_total_votu))*100
            fgl_persentajen = (fgl_total_votu/(jrh_total_votu+fgl_total_votu))*100
        except:
            jrh_total_votu = 1
            fgl_total_votu = 1
            jrh_persentajen = '0'
            fgl_persentajen = '0'

    context = {
        'apuramentu': apuramentu,
        'sentru_votasaun': sentru_votasaun,
        'somatoriu_votu': somatoriu_votu,
        'sentru_votasaun_hotu': sentru_votasaun_hotu,
        'sentru_id': id,
        'dahira_label': dahira_label,
        'jrh_total_votu': jrh_total_votu,
        'fgl_total_votu': fgl_total_votu,
        'jrh_persentajen': jrh_persentajen,
        'fgl_persentajen': fgl_persentajen,
        'ronda': ronda,
    }

    return context



def get_context_data_for_nivel(nivel, id, ronda):
    print('nivel')
    dahira_label = dahira_label
    apuramentu = ''
    somatoriu_votu = ''
    sentru_votasaun = "Timor-Leste"
    sentru_votasaun_hotu = SentruVotasaun.objects.all()
    jrh_total_votu = 50
    fgl_total_votu = 50
    jrh_persentajen = '50%'
    fgl_persentajen = '50%'
    
    if nivel == 'Natl': sentru_votasaun = "Nasionál" 
    else: sentru_votasaun = "Internasionál"

    if ronda == '6': 
        dahira_label = 'Volta Dahuluk (1)'
        apuramentu = Apuramentu.objects.filter(sentru_votasaun__nivel=nivel, eleisaun=ronda).values('kandidatu').order_by('-total_votu').annotate(total_votu=Sum('total_votu'))
        somatoriu_votu = Apuramentu.objects.filter(sentru_votasaun__nivel=nivel, eleisaun=ronda).aggregate(soma=Sum('total_votu'))['soma']
    else: 
        dahira_label = 'Volta Daruak (2)'
        jrh_total_votu = Apuramentu.objects.filter(eleisaun=ronda, sentru_votasaun__nivel=nivel, kandidatu='14').aggregate(total_votu_apuradu=Sum('total_votu'))['total_votu_apuradu']
        fgl_total_votu = Apuramentu.objects.filter(eleisaun=ronda, sentru_votasaun__nivel=nivel, kandidatu='6').aggregate(total_votu_apuradu=Sum('total_votu'))['total_votu_apuradu']
        
        try:
            jrh_persentajen = (jrh_total_votu/(jrh_total_votu+fgl_total_votu))*100
            fgl_persentajen = (fgl_total_votu/(jrh_total_votu+fgl_total_votu))*100
        except:
            jrh_total_votu = 1
            fgl_total_votu = 1
            jrh_persentajen = '0'
            fgl_persentajen = '0'

    sentru_votasaun_hotu = SentruVotasaun.objects.all()

    context = {
        'apuramentu': apuramentu,
        'sentru_votasaun': sentru_votasaun,
        'somatoriu_votu': somatoriu_votu,
        'sentru_votasaun_hotu': sentru_votasaun_hotu,
        'sentru_id': id,
        'dahira_label': dahira_label,
        'jrh_total_votu': jrh_total_votu,
        'fgl_total_votu': fgl_total_votu,
        'jrh_persentajen': jrh_persentajen,
        'fgl_persentajen': fgl_persentajen,
        'ronda': ronda,
    }
    
    return context



# @api_view(['GET'])
# def getPeopleList(request):
#     people = People.objects.all()
#     serializer = PeopleSerializer(people, many=True)
#     return Response(serializer.data)