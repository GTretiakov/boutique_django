from django.http import HttpResponse


class StripeWH_Handler:

    def __init__(self):
        self.request = request

    def handle_event(self, event):

        return HttpResponse(
            content=f'Webhook recived: {event["type"]}',
            status=200)
            