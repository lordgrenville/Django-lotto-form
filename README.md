# Scraping lotto numbers and displaying them - Django POC

The bulk of this repo is Django boilerplate, but the work I have done is in `lotto/views.py` and `lotto/templates/form.html`, as well as route mapping in
`lotto/urls.py`.

To run this app: from the project root run `python manage.py runserver`, and go to `127.0.0.1:8000/lotto/form`.

The form validates input, and if it is correct it passes an AJAX call to a scraper which fetches the results and places them on the page.
