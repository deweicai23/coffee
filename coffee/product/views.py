from django.shortcuts import render, get_object_or_404, redirect
from product.models import Product,Comment
from product.forms import ProductForm
from django.contrib import messages




def product(request):
    '''
    Render the article page
    '''
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'product/product.html',context)

def productRead(request, productId):
    '''
    Read an article
        1. Get the "article" instance using "articleId"; redirect to the 404 page if not found
        2. Render the articleRead template with the article instance and its
           associated comments
    '''
    product = get_object_or_404(Product, id=productId)
    context = {
        'product': product,
        'comments': Comment.objects.filter(product=product)
    }
    return render(request, 'product/productRead.html', context)


def productCreate(request):
    template = 'product/productCreateUpdate.html'
    if request.method == 'GET':
        return render(request, template, {'productForm':ProductForm()})
    
    
    
    # POST
    productForm = ProductForm(request.POST)
    if not productForm.is_valid():
        return render(request, template, {'productForm':productForm})

    productForm.save()
    messages.success(request, '產品已新增')
    return redirect('product:product')

def productUpdate(request, productId):
    product = get_object_or_404(Product, id=productId)
    template = 'product/productCreateUpdate.html'
    if request.method == 'GET':
        productForm = ProductForm(instance=product)
        return render(request, template, {'productForm':productForm})

    # POST
    productForm = ProductForm(request.POST, instance=product)
    if not productForm.is_valid():
        return render(request, template, {'productForm':productForm})

    productForm.save()
    messages.success(request, '文章已修改') 
    return redirect('product:productRead', productId=productId)


def productDelete(request, productId):
    
     if request.method == 'GET':
        return product(request)

    # POST
     product = get_object_or_404(Product, id=productId) 
     product.delete()
     messages.success(request, '文章已刪除')  
     return redirect('product:product')


