# Poll model ehlel


from django.contrib import admin
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Poll(models.Model):
    question = models.TextField()
    option_one = models.CharField(max_length=30)
    option_two = models.CharField(max_length=30)
    option_three = models.CharField(max_length=30)
    option_one_count = models.IntegerField(default=0)
    option_two_count = models.IntegerField(default=0)
    option_three_count = models.IntegerField(default=0)

    def total(self):
        return self.option_one_count + self.option_two_count + self.option_three_count

    class Meta:
        verbose_name = _("Санал асуулга")
        verbose_name_plural = _("Санал асуулга")
        ordering = ['question']


# Poll view ehlel


def home(request):
    polls = Poll.objects.all()
    context = {
        'polls': polls
    }
    return render(request, 'poll/home.html', context)


def vote(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)

    if request.method == 'POST':

        selected_option = request.POST['poll']
        if selected_option == 'option1':
            poll.option_one_count += 1
        elif selected_option == 'option2':
            poll.option_two_count += 1
        elif selected_option == 'option3':
            poll.option_three_count += 1
        else:
            return HttpResponse(400, 'Invalid form')

        poll.save()

        return redirect('poll:results', poll.id)

    context = {
        'poll': poll
    }
    return render(request, 'poll/vote.html', context)


@user_passes_test(lambda u: u.is_superuser)
def results(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    context = {
        'poll': poll
    }
    return render(request, 'poll/results.html', context)


class PollAdmin(admin.ModelAdmin):
    list_display = ['question']


admin.site.register(Poll, PollAdmin)
