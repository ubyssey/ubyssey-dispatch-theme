import json
from .forms import SubscriberForm
from .models import Subscriber
from django.http import HttpResponse
from django.views.generic import DeleteView
from bootstrap_modal_forms.generic import BSModalCreateView

class SubscriberCreateView(BSModalCreateView):
    """
    Class view for creating Subscribers through a form embedded in a bootstrap modal.
    Bootstrap modal and AJAX are intended to let this view to be used as long as a modal can be triggered, without refreshing or redirecting the page, so a user doesn't lose what they were reading.
    """
    form_class = SubscriberForm
    template_name = 'newsletter/subscribe.html'

    def post(self, request, *args, **kwards):
        """
        POST request is expected to use AJAX and will not redirect user to a different page

        This was based on this blog post (for reference): https://realpython.com/django-and-ajax-form-submissions/
        """
        response_data = {} # Dict that will hold stats of the submitted subscriber, or else let us know something odd happened, like a malformed POST request being made to the URL corresponding to this view
        form = self.get_form()
        if form.is_valid():
            subscribers_email = request.POST.get('email')        
            subscriber = Subscriber(email=subscribers_email)
            subscriber.save()

            response_data['result'] = 'Subscriber added!'
            response_data['subscriberpk'] = subscriber.pk
            response_data['email'] = subscriber.email
            # response_data['created'] = subscriber.created.strftime('%B %d, %Y %I:%M %p') #consider adding 'created' field so we can tell how old a subscriber is
        else:
            response_data['result'] = 'form.is_valid() check failed!'
        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )

class SubscriberDeleteView(DeleteView):
    form_class = SubscriberForm