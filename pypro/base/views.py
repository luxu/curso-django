import investpy
from django.http import JsonResponse
from django.shortcuts import render


def home(request):
    template_name = 'base/home.html'
    context = {}
    return render(request, template_name, context)


def trader(request, country, stock):
    template_name = 'base/home.html'
    context = {}
    if not country:
        country ='Brazil'
        stock = 'PETR4'
    df = investpy.get_stock_historical_data(
        stock=stock.upper(),
        country=country,
        from_date='01/01/2010',
        to_date='01/01/2020'
    )
    print(df.head())
    return JsonResponse(df.tail(), safe=False)


def investy(request):
    return render(request)
