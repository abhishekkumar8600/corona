from django.shortcuts import render

# Create your views here.
def home(request):
    news='hello'
    my_dict={'news':news}

    return render(request,'testapp/test.html',context=my_dict)
