from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, DeleteView
from . import forms
from . import models

class HomePageView(TemplateView):
    template_name = 'phonebook/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_by = self.request.GET.get('search_by')
        query = self.request.GET.get('query')
        search_message = "All phones"
        if search_by in ['phone', 'name'] and query:
            if search_by == 'name':
                search_message = f"Searching for 'name' by {query}"
                persones = models.Persone.objects.filter(name=query)
            else:
                persones = models.Persone.objects.filter(phones__phone__startswith=query)
                search_message = f"Searching for 'phone' by {query}"
            context["persones"] = persones
            context["search_message"] = search_message
            return context
        context["search_message"] = search_message
        context["persones"] = models.Persone.objects.all()
        return context



class AddPhoneFormView(CreateView):
    template_name = 'phonebook/add_persone.html'
    form_class = forms.CreatePersoneForm
    success_url = reverse_lazy('home')

    def get_success_url(self):
        phone_numbers = self.request.POST.get('phones')
        for phone_numbers in phone_numbers.split('\n'):
            models.Phone.objects.create(phone=phone_numbers, contact=self.object)

        return super().get_success_url()

class DeletePhoneView(DeleteView):
    model = models.Persone
    template_name = "phonebook/delete_persone.html"
    success_url = reverse_lazy('home')



