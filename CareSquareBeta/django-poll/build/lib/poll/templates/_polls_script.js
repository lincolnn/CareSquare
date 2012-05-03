{% load i18n %}

$(document).ready(function() {
	var vote_url = '{% url poll_ajax_vote poll.pk %}';
	var result_url = '{% url poll_ajax_result poll.pk %}';
	var poll_pk = '{{ poll.pk }}';
	var poll_type = '{{ poll_type }}';
	var can_vote = ('{{ can_vote }}' === 'True')? true : false;
	
	var path_to_items = '.dps_poll_content_' + poll_pk + ' .dps_poll_body input[name="poll_' + poll_pk + '"]';
	var body = $('.dps_poll_content_' + poll_pk + ' .dps_poll_body');
	
	function showResults(data) {
		var show_points = false;
		var all_points = 0, total = 0, biggest = 0;

		if(poll_type == 'Multiple') {
			show_points = true;
		}
		
		body.hide('slow', complete=function() {
			body.empty();
			$.each(data, function(index, value) {
				if(index != 'total') {
					if(data[index]['count'] > biggest) {
						biggest = data[index]['count'];
					}
					all_points += data[index]['count'];
				}
			});
			
			$.each(data, function(index, value) {
				if(index == 'total') {
					total = value;
				} else {
					var percentage = (data[index]['count'] * 100) / all_points;
					var bar_class = 'dps_poll_normal_bar';
					
					if(data[index]['count'] == biggest) {
						bar_class = 'dps_poll_max_bar';
					}
					
					var points_txt = '';
					if(show_points) {
						points_txt = '<sup>(' + data[index]['count'] + ')</sup>'; 
					}
					
					body.append('<dl class="dps_poll_item_dl">');
					body.append('<dt>' + data[index]['title'] + ': <strong>' + (Math.round(percentage*100)/100) + '%</strong>' + points_txt + '</dt>');
					body.append('<dd><div class="' + bar_class + '" style="width: ' + percentage + '%;"></div></dd>');
					body.append('</dl>');
				}
			});
			
			var total_points_txt = '';
			if(show_points) {
				total_points_txt = '<sup>(' + all_points + ')</sup>'; 
			}
			
			body.append('<div class="dps_poll_voters_count">' + trans_total_voters + ': <span class="dps_poll_total">' + total + '</span> ' + total_points_txt + '</div>');
		}).show('slow');
	}
	
	function RecognizeAndPrepare() {
		var result = '';
		
		$(path_to_items).map(function() {
			if((this.type == 'checkbox' || this.type == 'radio') && this.checked) {
				result += '"' + this.id + '": ' + '"' + this.type + '",';
			}
			if(this.type == 'text' && this.value != '') {
				result += '"' + this.id + '": ' + '"' + this.value + '",';
			}
		})
		
		if(result.length > 0)
			if(result[result.length - 1] == ',')
				result = result.substring(0, result.length - 1);
		
		return '{' + result + '}';
	}
	
	$(path_to_items).bind('focusin click', function() {
		if(poll_type == 'Single') {
			var selected = this;
			
			$(path_to_items).map(function() {
				if(this != selected) {
					if((this.type == 'checkbox' || this.type == 'radio') && this.checked) {
						this.checked = false;
					}
					if(this.type == 'text' && this.value != '') {
						this.value = '';
					}
				} 
			});
		}
	});
	
	function doResults() {
		$.get(result_url, function(data) {
			showResults($.parseJSON(data));
		});
	}
	
	$(".dps_sendvote_" + poll_pk).click(function() {
		var result = RecognizeAndPrepare();
		
		if(result == '{}') {
			alert(trans_choose_anything_to_vote);
		} else {
			if(!can_vote) {
				alert(trans_only_authenticated_users_can_vote);
				return;
			}
			body.hide('slow', complete=function() {
				$.get(vote_url, {'chosen_items': result}, function() {
					doResults();
				});
			});
		}
	});
	
	$(".dps_showresults_" + poll_pk).click(function() {
		doResults();
	});
});
