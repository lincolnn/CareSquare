from django.http import HttpResponse
from poll.models import Poll, Item, Vote, Choice
from django.db import transaction
from django.utils import simplejson
from utils import set_cookie

def authpass(user, queue):
    if queue != None:
        if queue.auth:
            if not user.is_authenticated():
                return False
    return True

#TODO: Need to optimize
@transaction.commit_on_success
def poll_ajax_vote(request, poll_pk):
    if request.is_ajax():
        try:
            poll = Poll.objects.get(pk=poll_pk)
            
            if poll.queue:
                if not authpass(request.user, poll.queue):
                    return HttpResponse('Non-authenticated users can\'t vote', status=400)
            
            chosen_items = simplejson.loads(request.GET['chosen_items'])
        except:
            return HttpResponse('Wrong parameters', status=400)
        
        if request.user.is_authenticated():
            user = request.user
        else:
            user = None
        
        vote = Vote.objects.create(poll=poll,
                                   ip=request.META['REMOTE_ADDR'],
                                   user=user)
        try:
            for item_pk, value in chosen_items.items():
                item = Item.objects.get(pk=item_pk)
                
                if item.userbox:
                    Choice.objects.create(vote=vote, item=item, uservalue=value)
                else:
                    Choice.objects.create(vote=vote, item=item)
        except:
            return HttpResponse('Data recognition failed', status=400)
        
        response = HttpResponse(status=200)
        set_cookie(response, poll.get_cookie_name(), poll_pk)
        
        return response
    return HttpResponse(status=400)

def poll_ajax_result(request, poll_pk):
    if request.is_ajax():
        try:
            poll = Poll.objects.get(pk=poll_pk)
        except:
            return HttpResponse('Wrong parameters', status=400)
        
        #Send data for results
        data = {}
        
        for item in Item.objects.filter(poll=poll):
            subdata = {
                       'index': item.index,
                       'title': item.value,
                       'count': Choice.objects.filter(item=item).count(),
                       }
            
            data[item.pk] = subdata
            
        data['total'] = Vote.objects.filter(poll=poll).count()
        
        return HttpResponse(simplejson.dumps(data))
    return HttpResponse(status=400)