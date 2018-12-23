from django.shortcuts import render


def product(request):
    '''
    Render the article page
    '''
    return render(request, 'product/product.html')