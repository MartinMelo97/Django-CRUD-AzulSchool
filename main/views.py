from django.shortcuts import render, redirect
from django import views
from .models import UserModel

class GetUsersView (views.View):
    def get(self, request):
        users = UserModel.objects.all()
        template_name = 'main/list.html'
        context = {
            'users': users
        }
        return render(request, template_name, context)

def GetUserView(request, id):
    user = UserModel.objects.get(pk=id)
    template_name = 'main/detail.html'
    context = {
        'user': user
    }
    return render(request, template_name, context)

class CreateUserView(views.View):
    template_name = 'main/form.html'
    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        gender = request.POST['gender']
        date_birth = request.POST['date_birth']

        if not date_birth:
            date_birth = None

        new_user = UserModel.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            gender=gender,
            date_birth=date_birth
        )

        if new_user:
            return redirect('/main')
        else:
            return render(request, self.template_name)

class UpdateUserView(views.View):
    template_name = 'main/form.html'
    def get(self, request, id):
        user = UserModel.objects.get(id=id)
        context = {
            'user': user
        }
        return render(request, self.template_name, context)

    def post(self, request, id):
        user = UserModel.objects.get(id=id)
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.phone_number = request.POST['phone_number']
        user.gender = request.POST['gender']
        user.date_birth = request.POST['date_birth']
        user.save()
        return redirect('/main/' + str(id))

def DeleteUserView(request, id):
    user = UserModel.objects.get(id=id)
    user.delete()

    return redirect('/main/')