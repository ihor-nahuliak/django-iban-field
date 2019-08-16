# django-iban-field
[![Build Status](https://travis-ci.org/ihor-nahuliak/django-iban-field.svg?branch=master)](https://travis-ci.org/ihor-nahuliak/django-iban-field)
[![Coverage Status](https://coveralls.io/repos/github/ihor-nahuliak/django-iban-field/badge.svg?branch=master)](https://coveralls.io/github/ihor-nahuliak/django-iban-field?branch=master)

Django model Field to store IBANs

The stored value is never fully visible.
Given an IBAN like "GR96 0810 0010 0000 0123 4567 890", 
the value is displayed as "---7890".

Superusers are able to see the full value when needed.

### Assumptions
* we talk about django model field, not about django form field
* we use global request object to check if current user is superuser,
  be careful with that!
* django admin panel needs additional form field behaviour describing
  (because the hidden value can't be simply shown in django admin edit view)
