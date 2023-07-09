from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView
from .models import *
from .models import Product_version
from .forms import ReviewForm
from django.db.models import Count, Q


class ProductListView(ListView):
    model = Product
    template_name = "product-list.html"
    paginate_by = 4
    context_object_name = "products"
    

    def get_queryset(self):
        category = self.request.GET.get("category")
        if category:
            return Product_version.objects.filter(product__category__p_category__name = category).order_by("date").all()
        search = self.request.GET.get("search")
        if search:
            products = Product_version.objects.filter(product__name__icontains = search)
            print("search value", search)
            print("products value", products)
            return products

        return (Product_version.objects.order_by("date").all(), products)

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.filter(is_navbar = "True").all()
        context['s_categories'] = Category.objects.filter(is_navbar = "False").all() 
        context['manufacturers'] = Manufacturer.objects.all()
        context['colors'] = Product_version.objects.values_list("color_id__name", flat=True).distinct().values('color_id__name').annotate(count = Count('color_id__name'))
        # context['products'] = Product.objects.all()
        
        return context


class ProductDetailView(DetailView, CreateView):
    template_name = 'product-detail.html'
    pk_url_kwarg = 'pk'
    model = Product
    context_object_name = "product"
    form_class = ReviewForm

    def get_object(self, queryset=None):
        product = Product_version.objects.get(pk=self.kwargs.get("pk"))
        product.read_count += 1
        product.save()
        return product
        
    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['images'] = Image.objects.all()
        context['r_items'] = Product_version.objects.filter(Q(product__category__p_category__name = kwargs['object'].product.category.p_category) | Q(product__category__name = kwargs['object'].product.category), ~Q(pk = self.kwargs.get("pk")), ~Q(product = kwargs["object"].product)).order_by('product').all().distinct('product')[:5]
        context['u_items'] = Product_version.objects.order_by("-review_count").filter(~Q(pk = self.kwargs.get("pk")), ~Q(product = kwargs["object"].product)).order_by('product').all().distinct('product')[:5]
        context['reviews'] = Review.objects.filter(product__pk = self.kwargs.get("pk")).all()[:3]
        context['colors'] = Product_version.objects.filter(product = kwargs["object"].product).all()
        return context
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = Product_version.objects.get(pk=self.kwargs.get("pk"))
            review.save()
            product = Product_version.objects.get(pk=self.kwargs.get("pk"))
            product.review_count += 1
            product.save()
        return redirect('product_detail', pk=self.kwargs.get("pk"))

# class ProductListView(ListView):
#     model = Product_version
#     template_name= "product-list.html"
#     context_object_name= "product_lists"
#     form_class = ReviewForm
#     paginate_by = 1

#     def get_queryset(self):  # sourcery skip: use-named-expression
#         color=self.request.GET.get('color')
#         size=self.request.GET.get('size')
#         manufacturer=self.request.GET.get('manufacturer')

#         if color:
#             self.queryset = product_version.objects.filter(color__name=color).all()

#         elif size:
#             self.queryset = product_version.objects.filter(size__name=size).all()
        
#         elif manufacturer:
#             self.queryset = product.objects.filter(manufacturer__name=manufacturer).all()
#         else:
#             self.queryset = Product_version.objects.all()

#         return self.queryset
