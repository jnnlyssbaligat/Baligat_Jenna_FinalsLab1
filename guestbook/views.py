from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import EntryForm
from .models import Entry


def guestbook(request):
    if request.method == "POST":
        # Bind the submitted data to the form so it can be validated.
        form = EntryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you! Your entry has been added.")
            return redirect("guestbook")
        # Invalid: fall through and re-render the bound form with form.errors.
    else:
        form = EntryForm()

    entries = Entry.objects.all()
    return render(request, "guestbook.html", {"form": form, "entries": entries})
