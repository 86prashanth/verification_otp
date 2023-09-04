from django.shortcuts import render,redirect
from todo_mail.models import Todo
from todo_mail.utils import send_email_to_user,send_email_to_attachment,SendEmail

# Create your views here.
def todo_create(request):
    context={}
    print('CALLED SEND EMAIL')
    # send_email_to_user("prashanthambala6@gmail.com","This is subject","hi my name is djagno send email")
    # send_email_to_attachment("prashanthambala6@gmail.com","This is subject","please find the attachment below")
    SendEmail('prashanthambala6@gmail.com','this is message','this is class ...')
    if request.method=='POST':
        todo=request.POST.get('todo')
        Todo.objects.create('todo')
        return redirect('')
    context['todos']=Todo.objects.all()
    return render(request,'todo_create.html',context)