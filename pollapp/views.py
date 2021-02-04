from django.shortcuts import render,redirect
from django.http import HttpResponse
from pollapp.forms import PollForm
from pollapp.models import Polldata

# Create your views here.

def index(request):
    polls = Polldata.objects.all()
    context = {
        'polls' : polls
    }
    return render(request,'home.html',context)

def createpoll(request):
    form = PollForm()
    context = {
        'form' : form
    }
    if request.method == "POST":
        form = PollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request,'create.html',context)    

def vote(request,pollid):
    poll = Polldata.objects.get(id=pollid)
    context = {
        'poll' : poll
    }

    if request.method == "POST":
        selectedis = request.POST['polls']
        if selectedis == "option1":
            poll.option1_count +=1
        elif selectedis == "option1":
            poll.option1_count +=1
        elif selectedis == "option1":
            poll.option1_count +=1        
        else:
            return HttpResponse("Invalid")

        poll.save()
        return redirect('result', poll.id)    
    return render(request,'vote.html',context)    

def result(request,pollid):
    poll = Polldata.objects.get(id=pollid)
    context = {
        'poll' : poll
    }

    return render(request,'result.html',context)   