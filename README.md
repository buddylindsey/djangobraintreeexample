# Braintree Django Integration - Example

This is a crude example of how to do braintree integration with django. This is just enough to get you a basic transaction in your braintree sandbox.

## Install and Run
### Install

```
git checkout https://github.com/buddylindsey/djangobraintreeexample.git
python3 -m venv ~/.virtualenvs/braintree
source ~/.virtualenvs/braintree/bin/activate
pip install -r requirements.txt
```

### Run
1. Add braintree settings to `cartintegration/settings.py`
2. `python manage.py runserver`
3. Visit [localhost:8000/checkout/](http://localhost:8000/checkout/)
4. Add credit card `4111 1111 1111 1111`
5. Expire `12/22`
6. Submit. If successful it should redirect to home page which will 404.
7. If transaction error it will spit out errors to console, and return back to checkout page.


## Resources
[Braintree Flask Example](https://github.com/braintree/braintree_flask_example)\
[Python Setup Your Server](https://developers.braintreepayments.com/start/hello-server/python)\
[Setup Your Client JS v3](https://developers.braintreepayments.com/start/hello-client/javascript/v3)

## License

### MIT

Copyright 2017 Buddy Lindsey, Jr.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.