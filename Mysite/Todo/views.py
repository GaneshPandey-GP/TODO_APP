from django.shortcuts import redirect,render,reverse
from .models import TODO
from .forms import CreateForm

def Create(request):
    post_list = TODO.objects.all().order_by('-timestamp')
    form = CreateForm()
    if request.method=='POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context ={'form':form,'post_list':post_list,}        
    return render(request,'Test/task_list.html',context)      

def Update(request,id):
    post_list = TODO.objects.get(id=id)
    form = CreateForm(instance=post_list)
    if request.method=='POST':
        form = CreateForm(request.POST,instance=post_list)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'Test/update_task.html',{'form':form})        


def deleteTask(request,id):
    post_list = TODO.objects.get(id=id)
    if request.method == 'POST':
        post_list.delete()
        return redirect('/')
    context = {' post_list': post_list}
    return render(request,'Test/delete_task.html',context)
 
