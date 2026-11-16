from django.db import models


class Entry(models.Model):
    """A single guestbook entry left by a visitor."""

    name = models.CharField(max_length=80)
    message = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "entries"

    def __str__(self):
        return f"{self.name}: {self.message[:40]}"
