from django.http import HttpResponse

class StripeWH_Handler:
    """ Handles Stripe Webhooks """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown or unexpected webhook event 
        """
        return HttpResponse(
            content=f'Unhandled Webhook recieved: {event["type2"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeed webhook from Stripe 
        """
        return HttpResponse(
            content=f'Webhook recieved: {event["type2"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe 
        """
        return HttpResponse(
            content=f'Webhook recieved: {event["type2"]}',
            status=200)

