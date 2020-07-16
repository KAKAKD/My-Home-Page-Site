from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import FormView
from mysite.form import ContactForm
from django.urls import reverse_lazy
from .models import WorkPost

# Create your views here.
class HomeView(TemplateView):
    template_name = "home.html"

class AboutView(TemplateView):
    template_name = "about.html"

class WorksView(ListView):
    template_name = "works.html"
    model = WorkPost
    paginate_by = 6

# Contact
class ContactFormView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = "contact_result"
    
    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)
    
class ContactResultView(TemplateView):
    template_name = 'contact_result.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['success'] = "メッセージは無事送信されました。"
        return context
