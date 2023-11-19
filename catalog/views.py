from django.contrib.auth.mixins import PermissionRequiredMixin
from django.forms import inlineformset_factory
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm, VersionForm, MProductForm
from catalog.models import Product, Version
from catalog.services import cache_category


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def contacts(request):
    return render(request, 'catalog/contacts.html')


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['version'] = Version.objects.filter(product=self.kwargs['pk'])
        return context


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index')

    def form_valid(self, form):
        if form.is_valid:
            new_product = form.save()
            new_product.user = self.request.user
            new_product.save()

        return super().form_valid(form)

    def get_queryset(self):
        return cache_category()


class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    permission_required = 'catalog.change_product'
    success_url = reverse_lazy('catalog:index')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if (self.request.user != self.object.user and not self.request.user.is_staff
                and not self.request.user.is_superuser and self.request.user.has_perm('catalog.product_published')):
            raise Http404
        return self.object

    def get_form_class(self):
        if self.request.user.has_perm('catalog.product_published'):
            return MProductForm
        return ProductForm


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:index')


class VersionListView(ListView):
    model = Version


