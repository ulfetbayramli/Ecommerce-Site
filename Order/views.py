from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.db.models import Q
from .forms import AddressInfoForm, BillingInfoForm, ShippingInfoForm, OrderForm
from .models import basket, basket_item, billing_addresses, shipping_addresses, wishlist
from Product.models import Product_version
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import CreateView, ListView
from django.views.generic.edit import FormMixin


class BillingInfo(LoginRequiredMixin, CreateView):
    form_class = BillingInfoForm
    success_url = reverse_lazy('index')
    template_name = 'billing_info.html'
    model = billing_addresses

    def get_context_data(self, **kwargs):
        context = super(BillingInfo, self).get_context_data(**kwargs)
        context['shipping_address'] = shipping_addresses.objects.filter(user_id = self.request.user).last()
        context['billing_address'] = billing_addresses.objects.filter(user_id = self.request.user).last()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            billing = form.save(commit=False)
            billing.user_id = self.request.user
            billing.save()
        messages.success(self.request, ('Your billing information has been successfully saved!'))
        return redirect('billing_info')

class ShippingInfo(LoginRequiredMixin, CreateView):
    form_class = ShippingInfoForm
    success_url = reverse_lazy('index')
    template_name = 'shipping_info.html'
    model = shipping_addresses

    def get_context_data(self, **kwargs):
        context = super(ShippingInfo, self).get_context_data(**kwargs)
        context['shipping_address'] = shipping_addresses.objects.filter(user_id = self.request.user).last()
        context['billing_address'] = billing_addresses.objects.filter(user_id = self.request.user).last()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            shipping = form.save(commit=False)
            shipping.user_id = self.request.user
            shipping.save()
        messages.success(self.request, ('Your shipping information has been successfully saved!'))
        return redirect('shipping_info')

class AddressInfo(LoginRequiredMixin, CreateView):
    form_class = AddressInfoForm
    success_url = reverse_lazy('index')
    template_name = 'address_info.html'
    model = shipping_addresses

    def get_context_data(self, **kwargs):
        context = super(AddressInfo, self).get_context_data(**kwargs)
        context['shipping_address'] = shipping_addresses.objects.filter(user_id = self.request.user).last()
        context['billing_address'] = billing_addresses.objects.filter(user_id = self.request.user).last()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user_id = self.request.user
            address.save()
            if address.is_billing == True:
                billing = billing_addresses(
                    first_name = form.cleaned_data.get('first_name'),
                    last_name = form.cleaned_data.get('last_name'),
                    telephone = form.cleaned_data.get('telephone'),
                    email = form.cleaned_data.get('email'),
                    street_address = form.cleaned_data.get('street_address'),
                    country = form.cleaned_data.get('country'),
                    city = form.cleaned_data.get('city'),
                    province = form.cleaned_data.get('province'),
                    zip = form.cleaned_data.get('zip'),
                    user_id = self.request.user
                )
                billing.save()
            if address.is_shipping == True:
                shipping = shipping_addresses(
                    first_name = form.cleaned_data.get('first_name'),
                    last_name = form.cleaned_data.get('last_name'),
                    telephone = form.cleaned_data.get('telephone'),
                    email = form.cleaned_data.get('email'),
                    street_address = form.cleaned_data.get('street_address'),
                    country = form.cleaned_data.get('country'),
                    city = form.cleaned_data.get('city'),
                    province = form.cleaned_data.get('province'),
                    zip = form.cleaned_data.get('zip'),
                    user_id = self.request.user
                )
                shipping.save()
        messages.success(self.request, ('Your address information has been successfully saved!'))
        return redirect('address_info')

class CheckoutView(LoginRequiredMixin, FormMixin, ListView):
    template_name = 'checkout.html'
    form_class = OrderForm
    model = Product_version
    context_object_name = 'addresses'
    
    def get_queryset(self):
        return billing_addresses.objects.filter(user_id = self.request.user).all()
        
    def get_context_data(self, **kwargs):
        context = super(CheckoutView, self).get_context_data(**kwargs)
        context['shipping_address'] = shipping_addresses.objects.filter(user_id = self.request.user).last()
        context['billing_address'] = billing_addresses.objects.filter(user_id = self.request.user).last()
        result = self.request.GET.get('result')
        products = basket_item.objects.filter(user = self.request.user).all()
        if result == "COMPLETED":
            for product in products:
                product.delete()
            user_basket =  basket.objects.filter(user = self.request.user, is_active = True).first()
            user_basket.is_active = False
            user_basket.save()
        grand_total = 0
        for product in products:
            grand_total += product.get_subtotal()
        context['grand_total'] = grand_total
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid(): 
            order_form = form.save(commit=False)
            order_form.user = self.request.user
            order_form.save()
        return redirect('index')

class BasketView(LoginRequiredMixin, ListView):
    model = basket
    template_name = 'shopping_cart.html'

    def get_context_data(self, **kwargs):
        context = super(BasketView, self).get_context_data(**kwargs)
        user_basket =  basket.objects.filter(Q(user = self.request.user), Q(is_active = True)).first()
        if user_basket:
            all_products = user_basket.items.all()
            context['baskets'] = all_products
        
        grand_total = 0
        products = basket_item.objects.filter(Q(user = self.request.user), Q(basket_items__is_active = True))
        for product in products:
            grand_total += product.get_subtotal()
        context['grand_total'] = grand_total
        return context
    
class WishlistView(LoginRequiredMixin, ListView):
    model = wishlist
    template_name = 'wishlist.html'

    def get_context_data(self, **kwargs):
        context = super(WishlistView, self).get_context_data(**kwargs)
        user_wishlist =  wishlist.objects.filter(user = self.request.user).first()
        if user_wishlist:
            all_products = user_wishlist.product.all()
            context['items'] = all_products
        return context

