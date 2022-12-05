import git
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView
from django.contrib.auth.forms import UserCreationForm
from .models import LinkDump, JsonDump
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
import os
from django.contrib import messages
import json
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError
from .tasks import sync_github
from celery.result import AsyncResult

User = get_user_model()


class HomeView(LoginRequiredMixin, CreateView):
    model = LinkDump
    fields = ['name', 'repo_link']
    template_name = 'index.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        kwargs['object_list'] = LinkDump.objects.order_by('date_created').filter(user=self.request.user)
        return super(HomeView, self).get_context_data(**kwargs)


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


@csrf_exempt
def gitsync(request):
    is_ajax = request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
    if request.POST.get("operation") == "gitsync" and is_ajax:

        sync = get_object_or_404(LinkDump, id=request.POST.get("content_id"))
        print(sync)
        repo_link = sync.repo_link
        user_home = os.path.expanduser('~')
        # Assuming git url is of form git@github.com:user/git-repo.git
        repo_name = repo_link[repo_link.rfind('/') + 1: repo_link.rfind('.')]
        abs_local_path = os.path.join(user_home, 'gitsync', repo_name)
        # clone the git repo
        res = sync_github.delay(repo_link, abs_local_path)
        print(res.id)
        # messages.success(request, res.get())
        for root, dirs, files in os.walk(abs_local_path):
            for file in files:
                if file.endswith('.json') and file not in ['metadata.json', 'pbr.json']:
                    location = root + '/' + str(file)
                    with open(location) as f:
                        json_string = f.read()
                    try:
                        # convert json string to python object
                        data = json.loads(json_string)
                        # save data to db
                        JsonDump.objects.create(**data, user=request.user, link=sync)
                        messages.success("json data has been added to Link dump db")
                    except json.decoder.JSONDecodeError:
                        messages.success(request, "Check Your Json File For Format Errors")
                    except IntegrityError:
                        messages.success(request, "Nope! You Cant Post The Same Data Twice")
    return JsonResponse({"task_id": res.id,
                         "sync_id":sync.id}, status=202)


@csrf_exempt
def get_status(request, task_id, sync_id):
    sync = LinkDump.objects.get(id=sync_id)
    task_result = AsyncResult(task_id)
    result = {
        "sync_id": sync_id,
        "task_id": task_id,
        "task_status": task_result.status,
        "task_result": task_result.result,

    }
    return JsonResponse(result, status=200)
