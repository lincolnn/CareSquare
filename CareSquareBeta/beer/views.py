from django.shortcuts import redirect
from django.shortcuts import render_to_response #provides response object
from django.template import RequestContext
from beer.models import Beer, Brewery #checkin.models import Member

def BeersAll(request): #spits out all Beers #def MembersAll(request):
        beers = Beer.objects.all().order_by('name') #returns list of all Beer objects in databse #members = Members.objects.all
        context = {'beers': beers} # 'beers' can be changed to whatever called in template.. link to the beers object response
        return render_to_response('beer/beersall.html', context, context_instance=RequestContext(request))

def SpecificBeer(request, beerslug): # def SpecificMember(request, memberslug):
    beer = Beer.objects.get(slug=beerslug) # member = Member.objects.get(slug=memberslug)
    context = {'beer': beer} #context = {'member': member}
    return render_to_response('beer/singlebeer.html', context, context_instance=RequestContext(request))
    # return render_to_response('singlemember.html', context, context_instance=RequestContext(request))

def SpecificBrewery(request, breweryslug):
        brewery = Brewery.objects.get(slug=breweryslug)
        beers = Beer.objects.filter(brewery=brewery)
        context = {'beers': beers}
        return render_to_response('beer/specificbrewery.html', context, context_instance=RequestContext(request))
