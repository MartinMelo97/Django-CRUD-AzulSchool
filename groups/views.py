from django.shortcuts import render, redirect
from django import views
from .models import Group
from .forms import GroupForm
from main.models import UserModel

def GetGroups(request):
    groups = Group.objects.all()
    template_name = 'groups/list.html'
    context = {
        'groups': groups
    }
    return render(request, template_name, context)

def GetGroup(request, id):
    group = Group.objects.get(pk=id)
    template_name = 'groups/detail.html'
    context = {
        'group': group
    }
    return render(request, template_name, context)


class CreateGroup(views.View):
    template_name = 'groups/form.html'
    action = 'create'
    def get(self, request):
        form = GroupForm()
        context = {
            'form': form,
            'action': self.action
        }
        return render(request, self.template_name, context)

    def post(self, request):
        new_form = GroupForm(request.POST)
        if new_form.is_valid():
            form_created = new_form.save()
            return redirect('groups:detail', form_created.id)
        else:
            context = {
                'form': new_form
            }
            return redirect(request, self.template_name, context)


class UpdateGroup(views.View):
    template_name = 'groups/form.html'
    action = 'update'

    def get(self, request, id):
        group = Group.objects.get(pk=id)
        form = GroupForm(instance=group)
        context = {
            'form': form,
            'group': group,
            'action': self.action
        }
        return render(request, self.template_name, context)

    def post(self, request, id):
        group = Group.objects.get(pk=id)
        edit_form = GroupForm(request.POST, instance=group)
        if edit_form.is_valid():
            form_updated = edit_form.save()
            return redirect('groups:detail', group.id)
        else:
            context = {
                'form': edit_form,
                'group': group,
                'action': self.action
            }
            return render(request, self.template_name, context)

def DeleteUser(request, id):
    user_id = request.POST.get('user_id')
    user = UserModel.objects.get(pk=user_id)
    group = Group.objects.get(pk=id)
    group.users.remove(user)
    return redirect('groups:detail', group.id)
