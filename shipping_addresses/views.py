from django.shortcuts import render, redirect
from django import views
from .models import ShippingAddress
from .forms import ShippingAddressForm
from main.models import UserModel

def GetShippingAddressView(request, id):
    address = ShippingAddress.objects.get(pk=id)
    context = {
        'address': address
    }
    template_name = 'shipping_addresses/detail.html'

    return render(request, template_name, context)

class CreateShippingAddressView(views.View):
    template_name = 'shipping_addresses/form.html'
    action = 'create'
    def get(self, request, user_id):
        address_form = ShippingAddressForm()
        user = UserModel.objects.get(pk=user_id)
        context = {
            'form': address_form,
            'action': self.action,
            'user': user
        }
        return render(request, self.template_name, context)

    def post(self, request, user_id):
        new_address = ShippingAddressForm(request.POST)
        user = UserModel.objects.get(pk=user_id)
        if new_address.is_valid():
            new_address_data = new_address.save(commit=False)
            new_address_data.user = user
            new_address_data.save()
            return redirect('addresses:detail', new_address_data.id)
        else:
            context = {
                'form': new_address,
                'action': self.action,
                'user': user
            }
            return render(request, self.template_name, context)

class UpdateShippingAddressView(views.View):
    template_name = 'shipping_addresses/form.html'
    action = 'update'
    def get(self, request, id):
        address = ShippingAddress.objects.get(pk=id)
        address_form = ShippingAddressForm(instance=address)
        context = {
            'form': address_form,
            'user': address.user,
            'address': address,
            'action': self.action
        }
        return render(request, self.template_name, context)

    def post(self, request, id):
        address = ShippingAddress.objects.get(pk=id)
        update_address_form = ShippingAddressForm(request.POST, instance=address)
        if update_address_form.is_valid():
            update_address_form.save()
            return redirect('addresses:detail', id)
        else:
            address_form = ShippingAddressForm(request.POST, instance=address)
            context = {
                'form': address_form,
                'user': address.user,
                'address': address,
                'action': self.action
            }
            return render(request, self.template_name, context)

def DeleteShippingAddressView(request, id):
    address = ShippingAddress.objects.get(pk=id)
    user = address.user
    address.delete()
    return redirect('user:detail', user.id)