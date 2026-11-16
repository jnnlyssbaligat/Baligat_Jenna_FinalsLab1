# Step-by-Step Guide: Web Guestbook (Week 13)

Everything below matches the project in `guestbook_project/`. The code is already written and tested
(7 passing tests), so your job is to run it, understand it, capture screenshots, and submit.

---

## Part 1 — Set up the project folder

Final folder layout:

```
guestbook_project/
├── manage.py
├── requirements.txt
├── README.md
├── .gitignore
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── guestbook/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── forms.py
    ├── models.py
    ├── tests.py
    ├── urls.py
    ├── views.py
    ├── migrations/
    │   └── 0001_initial.py
    ├── static/guestbook/style.css
    └── templates/guestbook.html
```

1. Unzip `guestbook_project.zip` somewhere easy (e.g. `Documents/PC15`).
2. Open the folder in VS Code (File → Open Folder → `guestbook_project`).
3. Open a terminal in VS Code (Ctrl + `) and create a virtual environment:
   - Windows: `python -m venv venv` then `venv\Scripts\activate`
   - macOS/Linux: `python3 -m venv venv` then `source venv/bin/activate`
4. Install Django: `pip install -r requirements.txt`
5. Create the database tables: `python manage.py migrate`
6. Create an admin account: `python manage.py createsuperuser` (any username/password you will remember)
7. Start the server: `python manage.py runserver`
8. Visit http://127.0.0.1:8000/ — you should see the dark purple guestbook.

> **Personalize it** (the sheet says not to copy as-is): change the page title/heading in
> `guestbook.html`, add your name to the footer, and/or tweak the accent colors in `style.css`
> (`--primary` and `--accent` at the top).

---

## Part 2 — Understand what each file does (be ready to explain)

| Task step in the sheet | Where it lives |
|---|---|
| 1. Model + ModelForm | `models.py` (`Entry`), `forms.py` (`EntryForm`, `Meta.model`, `Meta.fields`) |
| 2. View branches on `request.method` | `views.py` → `guestbook()` |
| 3. `{% csrf_token %}` in the form | `guestbook.html`, right after `<form method="post">` |
| 4. `is_valid()` before `save()` | `views.py` |
| 5. Invalid test shows `form.errors` | Blank field → page re-renders with red error text |
| 6. Valid test saves to DB | Entry appears on the page and in `/admin/` |

---

## Part 3 — Test and capture screenshots (for the PDF)

Take these **8 screenshots** (Windows: Win + Shift + S; macOS: Cmd + Shift + 4):

**Code (4):**
1. `forms.py` (whole file visible in VS Code)
2. `views.py`
3. `guestbook.html` (make sure the `{% csrf_token %}` line is visible)
4. `models.py`

**Output (4):**
5. **Blank-field error re-render** — leave *Name* (or *Message*) empty, click *Sign the Guestbook*. The page re-renders with a red error message. Include the browser address bar.
6. **Valid entry on the guestbook page** — submit a real name and message. Capture the green success message and the new entry card.
7. **Valid entry in Django Admin** — go to http://127.0.0.1:8000/admin/ → Entries; capture the list showing your entry.
8. **(Optional but impressive) CSRF proof** — in the browser, right-click the form → *View page source* and capture the hidden `csrfmiddlewaretoken` input. Or run `python manage.py test` and capture the terminal showing all tests passing (including `test_post_without_csrf_token_is_forbidden`).

---

## Part 4 — Build the PDF of screenshots

**Option A: Word / Google Docs (easiest)**
1. New blank document. Title: *Week 13 – Web Guestbook Output*, then your name, section, and date.
2. Add a heading **"Code"**, then paste screenshots 1–4, each with a one-line caption
   (e.g. *Figure 1. forms.py – EntryForm ModelForm*).
3. Add a heading **"Output"**, then paste screenshots 5–8 with captions
   (e.g. *Figure 5. Blank Name field re-renders with form.errors*).
4. Export: Word → File → Save As → PDF. Google Docs → File → Download → PDF Document.
5. Name it `Surname_Week13_Guestbook_Screenshots.pdf`.

**Option B: Print to PDF** — arrange the screenshots in any document and use *Print → Save as PDF*.

Check before submitting: every screenshot is readable (zoom in), and the PDF has both code and output.

---

## Part 5 — GitHub setup

### One-time (skip if you already have these)
1. Create an account at https://github.com.
2. Install Git: https://git-scm.com/downloads
3. Tell Git who you are:
   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "you@example.com"
   ```

### Create the repository
1. On GitHub: **+** (top right) → **New repository**.
2. Name: `django-web-guestbook`. Set it to **Public** (so your professor can open the link), or Private and add your professor as a collaborator.
3. **Do not** tick "Add a README" or ".gitignore" (the project already has them). Click **Create repository**.

### Push the project
Run these in the VS Code terminal, inside `guestbook_project/`:

```bash
git init
git add .
git status                      # confirm db.sqlite3 and venv/ are NOT listed
git commit -m "Add Week 13 Django guestbook with CSRF protection and validation"
git branch -M main
git remote add origin https://github.com/<your-username>/django-web-guestbook.git
git push -u origin main
```

If GitHub asks you to sign in, use the browser prompt, or a Personal Access Token as the password
(Settings → Developer settings → Personal access tokens).

### Verify
Open your repo URL. You should see `manage.py`, `config/`, `guestbook/`, `README.md`, and **no**
`db.sqlite3` or `venv/` folder. **This repo URL is what you submit** instead of the zip.

---

## Part 6 — Form Security Checklist (draft answers)

> Your instructor has their own Form Security Checklist template, which was not included in the PDF
> you shared. Use these answers to fill it in. If the wording differs, adapt it.

| Check | Done? | Evidence in your project |
|---|---|---|
| `{% csrf_token %}` inside every `<form method="post">` | ✅ | `guestbook.html`, first line inside the form |
| `CsrfViewMiddleware` enabled | ✅ | `config/settings.py` → `MIDDLEWARE` |
| Form uses POST (not GET) for data changes | ✅ | `<form method="post">` |
| View checks `request.method == 'POST'` | ✅ | `views.py` |
| Form bound with `EntryForm(request.POST)` | ✅ | `views.py` |
| `form.is_valid()` called before `form.save()` | ✅ | `views.py` |
| Raw `request.POST` is never saved directly | ✅ | Only `form.save()` writes to the DB |
| Only intended fields exposed | ✅ | `Meta.fields = ['name', 'message']` |
| Server-side validation (not just browser) | ✅ | `clean_name`, `clean_message`, `max_length`, `novalidate` on form |
| Errors shown on invalid input, no crash | ✅ | `field.errors` rendered under each field |
| Redirect after successful POST (no duplicate resubmits) | ✅ | `return redirect('guestbook')` |
| Output auto-escaped (XSS protection) | ✅ | Django templates escape `{{ entry.message }}` by default |
| Missing token → 403 Forbidden | ✅ | Verified by `test_post_without_csrf_token_is_forbidden` |

---

## Part 7 — Submission checklist

- [ ] Project zip **or** GitHub link (−25 pts if missing)
- [ ] PDF of screenshots, code + output (−15 pts if missing)
- [ ] Completed Form Security Checklist
- [ ] Submitted before the end of the lab session

## Troubleshooting

| Problem | Fix |
|---|---|
| `No module named django` | Activate the venv, then `pip install -r requirements.txt` |
| `no such table: guestbook_entry` | Run `python manage.py migrate` |
| 403 CSRF verification failed | `{% csrf_token %}` is missing or outside the `<form>` |
| Page has no styling | Make sure `runserver` is running with `DEBUG = True` |
| Font looks different | Inter loads from Google Fonts; offline it falls back to your system font |
