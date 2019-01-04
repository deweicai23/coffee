from django.contrib import admin

from product.models import Product, Comment,Order
class CommentModelAdmin(admin.ModelAdmin):
    list_display = ['product', 'content']
    list_filter = ['product', 'content']
    search_fields = ['content']
    list_editable = ['content']
 
    class Meta:
        model = Comment


admin.site.register(Product)
admin.site.register(Comment, CommentModelAdmin)
admin.site.register(Order)
