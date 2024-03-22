from django.http import HttpResponse

from quorum_app.builder import *
from quorum_app.render import *

# Create your views here.
def legislators_summary(request, output_format = 'plain'):
    legislators = build_legislators_summary()
    
    if (output_format == "json"):
        response = render_legislators_as_json(legislators)
    else:
        response = render_legislators_as_simple_html(legislators)

    return HttpResponse(response)

def bills_summary(request, output_format = 'plain'):
    bills = build_bills_summary()

    if (output_format == "json"):
        response = render_bills_as_json(bills)
    else:
        response = render_bills_as_simple_html(bills)

    return HttpResponse(response)
