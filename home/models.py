from django.db import models


class Home(models.Model):
    """Home model

    ---
    Attributes:
        content : introductory text to the site
        address : physical address and contact details
    """

    content = models.TextField()
    address = models.TextField()

    def __str__(self):
        """Returns `content`"""
        return self.content
