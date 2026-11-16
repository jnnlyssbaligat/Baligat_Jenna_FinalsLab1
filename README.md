# Web Guestbook (Django) — Week 13

A CSRF-protected guestbook built with a Django `ModelForm`. Submissions are validated with
`form.is_valid()` before being saved.

## Run it

```bash
python -m venv venv
venv\Scripts\activate          # Windows   (macOS/Linux: source venv/bin/activate)
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser   # optional, for /admin/
python manage.py runserver
```

Open http://127.0.0.1:8000/ for the guestbook and http://127.0.0.1:8000/admin/ for Django Admin.

## Run the tests

```bash
python manage.py test
```

## Structure

| File | Purpose |
|------|---------|
| `guestbook/models.py` | `Entry` model (name, message, created_at) |
| `guestbook/forms.py` | `EntryForm` ModelForm + validation |
| `guestbook/views.py` | Branches on `request.method`; saves only if `is_valid()` |
| `guestbook/templates/guestbook.html` | Form with `{% csrf_token %}` and entries list |
| `guestbook/static/guestbook/style.css` | Dark purple theme |

Course: PC15 Python Programming 2 w/ Lab — National Teachers College
