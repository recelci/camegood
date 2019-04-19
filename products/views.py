from django.shortcuts import render, get_object_or_404, redirect

from .models import Product
from .forms import ProductForm, RawProductForm
# Create your views here.


def product_create_view(request):

    form = ProductForm(request.POST or None)

    if form.is_valid():
        form.save()
        form= ProductForm()
   
    context = {

        'form': form

    }
    return render(request, "products/product_create.html", context)



#DON'T NEED TO USE THIS AS VIEW
# def product_create_view(request):
#     my_form = RawProductForm()

#     if request.method == "POST":
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             print(my_form.cleaned_data)
#             Product.objects.create(**my_form.cleaned_data)
#         else:
#             print(my_form.errors)
    
#     context = {
#         "form": my_form
#     }
#     return render(request, "products/product_create.html", context)



# RAW FORM (BAD APPROACH)
# def product_create_view(request):

#     if request.method == "POST":
#         my_new_title = request.POST.get('title')
#         print(my_new_title)
    
#     context = {}

#     return render(request, "products/product_create_v2.html", context)




def product_detail_view(request, id):

    print(request.user)

    if not request.user.is_authenticated:
        print(request.user)
        return render(request, "about.html")

    # obj = Product.objects.get(id=id)
    obj = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance= obj)

    if form.is_valid():
        form.save()


    context = {
        'form': form
    }

    return render(request, "products/product_detail.html", context)


def product_delete_view(request, id):

    print(request.user)
    print(request.method)
    if not request.user.is_authenticated:
        print(request.user)
        return render(request, "about.html")

    # obj = Product.objects.get(id=id)
    obj = get_object_or_404(Product, id=id)
    
    if request.method=="POST":
        print(obj)
        obj.delete()
        return redirect('products')

    context = {
        'object': obj
    }

    return render(request, "products/product_delete.html", context)


def product_list_view(request):

    print(request.user)

    queryset=Product.objects.all()

    if not request.user.is_authenticated:
        print(request.user)
        return render(request, "about.html")

    context = {
        'object_list': queryset
    }

    return render(request, "products/products.html", context)


# def product_detail_view(request):

#     obj = Product.objects.get(id=1)

#     # context = {
#     #     'title': obj.title,
#     #     'price': obj.price,
#     # }

#     context = {

#         'object': obj

#     }
#     return render(request, "products/product_detail.html", context)