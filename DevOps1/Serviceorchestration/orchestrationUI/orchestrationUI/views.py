from django import forms
from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from django.http import HttpResponse

# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

def my_view(request):
    # View code here...
    t = loader.get_template('index.html')
    c = RequestContext(request, {'foo': 'bar'})
    response=HttpResponse(t.render(c))
    print "RESPONSE IS :: -->"+str(response)
    logger.info(response)
    return response 


def my_view1(request):
    # View code here...
    t = loader.get_template('vnfd.html')
    table=['name','value','time'] 
    mylst = [{'name':'myname','value':'30','time':'202020'},{'name':'myname1','value':'myname10','test':'20'}]
    c = RequestContext(request, {'mylst': mylst,'table':table})
    return HttpResponse(t.render(c))


def my_view2(request):
    # View code here...
    t = loader.get_template('vld.html')
    c = RequestContext(request, {'foo': 'bar'})
    return HttpResponse(t.render(c))


def my_view3(request):
    # View code here...
    t = loader.get_template('vnffgd.html')
    c = RequestContext(request, {'foo': 'bar'})
    return HttpResponse(t.render(c))


def my_view4(request):
    # View code here...
    t = loader.get_template('nsd.html')
    c = RequestContext(request, {'foo': 'bar'})
    return HttpResponse(t.render(c))


class UploadForm(forms.Form):
    name = forms.CharField(max_length=256)
    description = forms.CharField(max_length=256)
    file_name = forms.FileField()
    


def my_view5(request):
    # View code here...
    form=UploadForm()
    t = loader.get_template('_create_template.html')
    c = RequestContext(request, {'form': form})
    return HttpResponse(t.render(c))


def _work(request):
    # View code here...
    form=UploadForm()
    t = loader.get_template('_work_template.html')
    c = RequestContext(request, {'form': form})
    return HttpResponse(t.render(c))



def create_vnf(request):
    
    #print request
    #import pdb;pdb.set_trace()
    form = UploadForm(request.POST, request.FILES)
    if form.is_valid():
            print "Got cpk",form.cleaned_data['name']
            print "Got file",request.FILES['file_name'].read() 

    file_name=request.FILES['file_name']

    file1 = request.FILES['file_name']
    
    filename = str(file1)
    with open(filename, 'wb+') as destination:
        for chunk in file1.chunks():
            destination.write(chunk)
     #                filepath = os.path.abspath(newfile.txt)
     #   with open('newfile.txt', 'rb+') as destination1:
     #       print destination1.read()         

    try:
        url = 'http://127.0.0.1:5070/on-board-vnfd'
        register_openers()
        #params = request.FILES[str(file1)].read()
        #params = csv.DictReader(paramFile)

        params = {'vnfd_file' : open(filename, "rb")}
        datagen, headers = multi_part_encode(params)
        request1 = urllib2.Request(url, datagen, headers)
        response = urllib2.urlopen(request1).read()
    except:
        response="NOT FOUND"
    return HttpResponse(response)
    print response

   

