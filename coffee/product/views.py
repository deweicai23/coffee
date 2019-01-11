from django.shortcuts import render, get_object_or_404, redirect
from product.models import Product,Comment
from product.forms import ProductForm,OrderForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from main.views import admin_required




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

@admin_required
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


@admin_required
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
    messages.success(request, '產品已修改') 
    return redirect('product:productRead', productId=productId)

@admin_required
def productDelete(request, productId):
    
     if request.method == 'GET':
        return product(request)

    # POST
     product = get_object_or_404(Product, id=productId) 
     product.delete()
     messages.success(request, '產品已刪除')  
     return redirect('product:product')
 
@login_required 
def productLike(request, productId):
    product = get_object_or_404(Product, id=productId)
    if request.user not in product.likes.all():
        product.likes.add(request.user)
    return productRead(request, productId)

@login_required
def commentCreate(request, productId):
    '''
    Create a comment for an article:
        1. Get the "comment" from the HTML form
        2. Store it to database
    '''
    if request.method == 'GET':
        return productRead(request, productId)

    # POST
    comment = request.POST.get('comment')
    if comment:
        comment = comment.strip()
    if not comment:
        return redirect('product:productRead', productId=productId)

    product = get_object_or_404(Product, id=productId)
    Comment.objects.create(product=product, user=request.user, content=comment)
    return redirect('product:productRead', productId=productId)

@login_required
def commentDelete(request, commentId):
   
    comment = get_object_or_404(Comment, id=commentId)
    product = get_object_or_404(Product, id=comment.product.id)
    if request.method == 'GET':
        return productRead(request, product.id)

    # POST
    if comment.user != request.user:
        messages.error(request, '無刪除權限')
        return redirect('product:productRead', productId=product.id)

    comment.delete()
    return redirect('product:productRead', productId=product.id)

@login_required
def commentUpdate(request, commentId):
    
    commentToUpdate = get_object_or_404(Comment, id=commentId)
    product = get_object_or_404(Product, id=commentToUpdate.product.id)
    if request.method == 'GET':
        return productRead(request, product.id)

    # POST
    if commentToUpdate.user != request.user:
        messages.error(request, '無修改權限')
        return redirect('product:productRead', productId=product.id)

    comment = request.POST.get('comment', '').strip()
    if not comment:
        commentToUpdate.delete()
    else:
        commentToUpdate.content = comment
        commentToUpdate.save()
    return redirect('product:productRead', productId=product.id)

def productOrder(request):
    template = 'product/productOrder.html'
    if request.method == 'GET':
        return render(request, template, {'orderForm':OrderForm()})
    
    
    
    # POST
    orderForm = OrderForm(request.POST)
    if not orderForm.is_valid():
        return render(request, template, {'orderForm':OrderForm})

    orderForm.save()
    messages.success(request, '產品已订购')
    return redirect('product:product')
       


