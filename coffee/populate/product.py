from populate import base
from account.models import User
from product.models import Product, Comment


titles = ['冷酿造', '香草味甜奶油酿造', '焦糖玛奇朵']
comments = ['超级顺滑，带有巧克力和柑橘味。', '只是一个飞溅，更甜美，更光滑的完成。', '味道更好', '如此迷惑']

def populate():
    print('Populating articles and comments ... ', end='')
    Product.objects.all().delete()
    Comment.objects.all().delete()
    
    
    admin = User.objects.get(is_superuser=True)
    for title in titles:
        product = Product()
        product.title = title
        for j in range(20):
            product.content += title + '\n'
        product.save()
        for comment in comments:
            Comment.objects.create(product=product, user=admin, content=comment)
    print('done')


if __name__ == '__main__':
    populate()