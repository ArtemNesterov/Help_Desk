from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from help_desk import form
from help_desk.models import ClaimModel, CommentModel


class ClaimListView(ListView):
    model = ClaimModel
    template_name = 'claims_list.html/'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_staff:
                qsetadmin = Q(status='PN') | Q(status='IP')
                return ClaimModel.objects.filter(qsetadmin)
            else:
                return ClaimModel.objects.filter(author=self.request.user)

    def post(self, request, *args, **kwargs):
        claim_id = request.POST.get('claim_id', '')
        claim = ClaimModel.objects.get(pk=claim_id)
        if 'decline' in request.POST:
            claim.status = 'DC'
            claim.declined_status_count += 1
        elif 'done' in request.POST:
            claim.status = 'DN'
        elif 'confirm' in request.POST:
            claim.status = 'IP'
        else:
            claim.status = 'PN'
        claim.save()
        return HttpResponseRedirect()


class ClaimDetailView(DetailView):
    model = ClaimModel

    def post(self, request, *args, **kwargs):
        claim_id = request.POST.get('claim_id', '')
        claim = ClaimModel.objects.get(pk=claim_id)
        if 'decline' in request.POST:
            claim.status = 'DC'
            claim.declined_status_count += 1
        elif 'done' in request.POST:
            claim.status = 'DN'
        elif 'confirm' in request.POST:
            claim.status = 'IP'
        else:
            claim.status = 'PN'
        claim.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class NewClaimView(CreateView):
    model = ClaimModel
    form_class = form.NewClaimForm
    success_url = reverse_lazy('claims_list_page')

    def form_valid(self, form):
        self.object = form.save()
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


"""
reverse_lazy- for regulars and pattern changes (url)
"""


class EditClaimView(UpdateView):
    model = ClaimModel
    form_class = form.EditClaimForm
    success_url = reverse_lazy('claims_list_page')


class ClaimDeleteView(DeleteView):
    model = ClaimModel
    success_url = reverse_lazy('claims_list_page')


class NewCommentView(CreateView):
    model = CommentModel
    form_class = form.CommentForm
    success_url = reverse_lazy('claims_list_page')

    def get_initial(self):
        initial = {'claim': self.kwargs.get('pk')}
        return initial

    def form_valid(self, form):
        self.object = form.save()
        self.object.author = self.request.user
        self.object.claim_id = form.initial.get('claim')
        self.object.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, 'Invalid DATA')
        return super(NewCommentView, self).form_invalid(form)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            if self.request.user.is_staff:
                claim_id = self.kwargs.get('pk')
                claim = ClaimModel.objects.get(pk=claim_id)
                claim.status = 'DC'
                claim.declined_status_count += 1
                claim.save()
            else:
                return self.form_valid(form)
        else:
            return self.form_invalid(form)

