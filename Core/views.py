from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import CreateView, ListView
from .models import FAQ
from Blog.models import Blog
from Product.models import Product_version, Product
from .forms import ContactUsForm
from django.db.models import Count, Q
from Product.views import ProductListView
from django.views.generic import ListView, DetailView, CreateView
from Product.models import *
from Product.models import Product_version
from Product.forms import ReviewForm
from django.db.models import Count, Q


# Create your views here.
def searchview(request):
    s = request.GET['ssss']
    print("searched value", s)

    # category = self.request.GET.get("category")
    # if category:
    #     return Product_version.objects.filter(product__category__p_category__name = category).order_by("date").all()
    # return Product_version.objects.order_by("date").all()

    product1 = Product.objects.all()
    if s:
        product1 = product1.filter(Q(name__icontains=s))
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print(product1)
    else:
        product1 = Product.objects.all()

    # context['categories'] = Category.objects.filter(is_navbar = "True").all()
    # context['s_categories'] = Category.objects.filter(is_navbar = "False").all() 
    # context['manufacturers'] = Manufacturer.objects.all()
    # context['colors'] = Product_version.objects.values_list("color_id__name", flat=True).distinct().values('color_id__name').annotate(count = Count('color_id__name'))
    # context['products'] = product1


    context = {
        'product_list': product1,
    }
    return render(request, 'i.html', context)




class HomePage(ListView):
    template_name = 'index.html'
    model = Blog
    context_object_name = 'blogs'

    def get_queryset(self):
        return Blog.objects.order_by("-date").all()[:2]

    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        context['items'] = Product_version.objects.order_by("date").all()[:10]
        context['featured_items'] = Product_version.objects.order_by( "read_count").all()[:4]
        context['best_items'] = Product_version.objects.order_by( "review_count").all()[:4]
        context['new_items'] = Product_version.objects.order_by( "date").all()[:4]
        return context

class ContactUs(CreateView):
    template_name = 'contact_us.html'
    form_class = ContactUsForm

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Your comment has been sent successfully!')
        return redirect('contact_us')

class FAQ(ListView):
    template_name = 'faq.html'
    model = FAQ
    context_object_name = 'faqs'

def error(request):
    return render(request, "404error.html")
    
def about_us(request):
    return render(request, "about_us.html")