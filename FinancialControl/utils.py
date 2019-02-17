from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import *


class ObjectDetailMixin:
    model = None
    template = None

    def get(self,requst,slug):
        object = get_object_or_404(self.model, slug__iexact=slug)
        return render(requst, self.template, context={self.model.__name__.lower(): object})