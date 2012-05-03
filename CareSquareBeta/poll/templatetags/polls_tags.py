from django import template
from poll.models import Poll, Item, Queue
from settings import STATIC_URL
from django.utils.safestring import SafeUnicode
from django.utils.datetime_safe import datetime
from poll.ajax import authpass

register = template.Library()
@register.inclusion_tag('polls.html', takes_context=True)
def poll(context, poll):
    can_vote = True
    if poll.queue:
        can_vote = authpass(context['user'], poll.queue)
    return {'poll': poll, 'poll_type': poll.print_polltype(), 'items': Item.objects.filter(poll=poll), 'user': context['user'], 'can_vote': can_vote, 'request': context['request'], 'STATIC_URL': STATIC_URL}

@register.inclusion_tag('polls.html', takes_context=True)
def poll_queue(context, queue):
    try:
        if isinstance(queue, SafeUnicode):
            tmp_queue = Queue.objects.get(title=queue)
        else:
            tmp_queue = Queue.objects.get(queue)
    except:
        raise Exception('Queue not found')
    
    tmp_polls = Poll.publish_manager.filter(queue=tmp_queue, startdate__lte=datetime.now())
    
    if len(tmp_polls) > 0:
        cur_poll = tmp_polls[0]
    else:
        cur_poll = None
    
    return poll(context, cur_poll)

class RenderItemsClass(template.Node):
    def __init__(self, poll, items):
        self.poll=template.Variable(poll)
        self.items=template.Variable(items)
        
    def render(self, context):
        poll = self.poll.resolve(context)
        items = self.items.resolve(context)
        #'name' = item.pk
        pattern1 = '{3}<br /><input name="poll_{0}" type="{1}" id="{2}" value="" /><br />'
        pattern2 = '<input name="poll_{0}" type="{1}" id="{2}" /> {3}<br />'
        result = ''
        
        #Choose an input type
        for item in items:
            if item.userbox:
                input_type = 'textbox'
                pattern = pattern1
            else:
                poll_type = poll.print_polltype()
                
                if poll_type == 'Single':
                    input_type = 'radio'
                elif poll_type == 'Multiple':
                    input_type = 'checkbox'
                pattern = pattern2
                    
            result += pattern.format(poll.pk, input_type, item.pk, item.value)
            
        return result

@register.tag
def render_items(parser, token):
    tag, poll, items = token.split_contents()
    return RenderItemsClass(poll, items)