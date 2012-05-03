# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from checkin.models import Members, Rating

def MembersAll(request):
    members = Members.objects.all().order_by('name')
    context = {'members': members}
    return render_to_response('membersall.html', context, context_instance=RequestContext(request)

def SpecificMember(request, memberslug):
    member = Member.objects.get(slug=memberslug)
    context = {'member': member}
    return render_to_response('singlemember.html', context, context_instance=RequestContext(request))

def SpecificRating(request, ratingslug):
    rating = Rating.ojects.get(slug=rating)
    members = Memebr.objects.filter(rating=rating)
    context = {'members': members}
    return render_to_response('singlerating.html', context, context_instance=RequestContext(request))
