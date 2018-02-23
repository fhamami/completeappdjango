from django.shortcuts import render
from django.views.generic import View
from django.template import loader
from django.http import HttpResponse

from .models import Item, Category

def categories(request):
    context = {
        'categories': Category.objects.all()
    }
    return render(request, 'foreignkey/category.html', context)

def items(request, item_id):
    try:
        itm = Item.objects.get(id=item_id)
    except Item.DoesNotExist:
        itm = None

    template = loader.get_template('foreignkey/itemdetails.html')
    context = {
        'item': itm
    }
    return HttpResponse(template.render(context, request))
    # user_list = balance.objects.filter(user=request.user)
    # return render(request, 'foreignkey/app.html', {'section': 'Item'})