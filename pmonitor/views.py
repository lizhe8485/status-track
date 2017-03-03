from django.shortcuts import render
from django.utils import timezone
# Create your views here.
#from django.http import HttpResponse
#from django.template import loader
from .models import Status
from .forms  import propertyForm

def index(request):
    #template = loader.get_template('pmonitor/index.html')
    status_list = Status.objects.all().order_by('component')[0:10]

    #status_list2 = [{'sampleName':'',},{}] #a new status list with status code of each part
    form = propertyForm()
    context = {'greeting':'Status of ATP components','status_list':status_list,'form':form,'range':range(9),'showList':range(10)}
    return render(request,'pmonitor/index.html',context)

def status_list(request):
    myfilter = request.POST['tableFilter']
    mysample = request.POST['searchsample']
    if myfilter == "all":
       samplesList = Status.objects.all()
    if myfilter =="start":
       samplesList = Status.objects.filter(MethodGeneration='started')
    if myfilter =="complete":
       samplesList = Status.objects.filter(postProcess='finished')
    if myfilter =="error":
       samplesList = Status.objects.filter(postProcess='error')
    if mysample:
       samplesList = Status.objects.filter(SampleName=mysample)

    statusList = []
    for entry in samplesList:
       statusList.append(entry.aStatusList)
    statusDict = {'greeting':'Welcome to ATP Process Monitor','message':'filtered sampleruns','range':range(9),'statusList':statusList}

    return render(request,'pmonitor/status_list.html',{'statusDict':statusDict})

def short_status_list(request):
    samplesList = Status.objects.all() #.order_by() or filter(time > **)
    aList = ["MethodGeneration","DAMethodGeneartion","Acquisition","FileMover","Preprocess","DataAnalysis","ReportReader","CSVGeneration","postProcess"]
    shortstatusList = []
    for entry in samplesList:
       shortstatusList.append(entry.aStatusList)       
    statusDict = {'aList':aList,'shortstatusList':shortstatusList}

    return render(request,'pmonitor/short_status_list.html',{'statusDict':statusDict})
    
def detail(request, status_id):
    return render(request,'pmonitor/detail.html',{'id':status_id})

def predict(request):
    form = propertyForm()
    return render(request,'pmonitor/predict.html',{'form':form})

def results(request):
    isvalidForm = False
    method = 'failed to get a method'
    if request.method == 'POST':
       form = propertyForm(request.POST)
       if form.is_valid():
          isvalidForm = True
          method = 'HPLC, HILIC, Positive ION'
    else:
       form = propertyForm()
    resultDict= {'greeting':'Welcome to AMP Analytical Method Predictor','message':'Show Predicted Method','isvalidform':isvalidForm,'method':method,'form':form} 
    return render(request,'pmonitor/results.html',resultDict)
