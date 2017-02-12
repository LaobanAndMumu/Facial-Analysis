from django.shortcuts import render
from django.http import Http404

from firstapp.models import Analysis

def index(request):
    features = Analysis.objects.all()
    return render(request, 'analysis/index.html',{
        'features':features,
    })

def analysis_detail(request,id):
    try:
        feature = Analysis.objects.get(id=id)
    except Analysis.DoesNotExist:
        raise Http404('This feature does not exist')
    return render(request, 'analysis/analysis_detail.html',{
        'feature':feature,
    })