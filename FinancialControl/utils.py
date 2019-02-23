from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse


class ObjectDetailMixin:
    model = None
    template = None

    def get(self, requst, slug):
        object = get_object_or_404(self.model, slug__iexact=slug)
        return render(requst, self.template, context={self.model.__name__.lower(): object})


class ObjectAddMixin:
    model_form = None
    template = None

    def get(self, request):
        form = self.model_form
        return render(request, self.template, context={'form': form})

    def post(self, request):
        bound_form = self.model_form(request.POST)

        if bound_form.is_valid():
            new_object = bound_form.save()
            return redirect(new_object)
        return render(request, self.template, context={'form': bound_form})


class ObjectUpdateMixin:
    model = None
    model_form = None
    template = None

    def get(self, request, slug):
        object = self.model.objects.get(slug__iexact=slug)
        bound_form = self.model_form(instance=object)
        return render(request, self.template, context={'form': bound_form, self.model.__name__.lower(): object})

    def post(self, request, slug):
        object = self.model.objects.get(slug__iexact=slug)
        bound_form = self.model_form(request.POST, instance=object)

        if bound_form.is_valid():
            update_object = bound_form.save()
            return redirect(update_object)
        return render(request, self.template, context={'form': bound_form, self.model.__name__.lower(): object})


class ObjectDeleteMixin:
    model = None
    template = None
    redirect_url = None

    def get(self, request, slug):
        object = self.model.objects.get(slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower(): object})

    def post(self, reuqest, slug):
        object = self.model.objects.get(slug__iexact=slug)
        object.delete()
        return redirect(reverse(self.redirect_url))
