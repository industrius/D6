from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from .models import Pet, Recall, Comment
from .forms import RecallFrom, CommentForm

class PetList(ListView):
    model = Pet
    template_name = "pets_list.html"

class PetDetails(DetailView):
    model = Pet
    template_name = "pet_details.html"

    def post(self, request, pk):
        pet_object = Pet.objects.filter(id=pk).first()
        note = request.POST["note"]
        pet_object.comment.create(note=note)
        return HttpResponseRedirect("/pet/"+pk)

class About(TemplateView):
    template_name = "about.html"

def RecallList(request):
    recall_list = Recall.objects.all()
    if request.method == "POST":
        form = RecallFrom(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/recall")
    else:
        form = RecallFrom()
    return render(request, "recall_list.html", {"recall_form": form, "recall_list": recall_list})