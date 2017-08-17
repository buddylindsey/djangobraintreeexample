from django.views.generic import FormView


from django import forms
from django.conf import settings

import braintree

class BraintreeSaleForm(forms.Form):
    amount = forms.DecimalField(decimal_places=2, max_digits=20)
    payment_method_nonce = forms.CharField()


class CheckoutView(FormView):
    template_name = 'checkout.html'
    success_url = '/'
    form_class = BraintreeSaleForm

    def get_context_data(self, **kwargs):
        braintree.Configuration.configure(braintree.Environment.Sandbox,
                                          merchant_id=settings.BRAINTREE_MERCHANT_ID,
                                          public_key=settings.BRAINTREE_PUBLIC_KEY,
                                          private_key=settings.BRAINTREE_PRIVATE_KEY)

        context = super().get_context_data(**kwargs)
        context['client_token'] = braintree.ClientToken.generate()
        return context

    def form_valid(self, form):
        amount = form.cleaned_data['amount']
        nonce = form.cleaned_data['payment_method_nonce']

        result = braintree.Transaction.sale({
            "amount": amount,
            "payment_method_nonce": nonce,
            "options": {
                "submit_for_settlement": True
            }
        })

        if result.is_success or result.transaction:
            print(result.transaction)
            return super().form_valid(form)
        else:
            print(result.errors)
            return super().form_invalid(form)