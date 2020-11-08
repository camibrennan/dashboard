from django.db import models

# Create your models here.
class DashboardPanel(models.Model):
# For the GitHub example:
    github_username = models.CharField(max_length=127)
    repo_name = models.CharField(max_length=127)
# Customizable aspects of panel chart
    panel_type = models.CharField(max_length=127, choices=[
    ("piechart", "Pie-chart of languages used"),
    ("barchart", "Bar-chart of languages used"),
    ])
# TODO: More fields might go here...
# (Consider adding other customizable aspects, including style or theme,
# different chart options, text descriptions.)