from celery import shared_task
import git
from git import Repo
from celery_progress.backend import ProgressRecorder
import time

@shared_task(bind=True)
def sync_github(self, repo_link, abs_local_path):
    progress_recorder = ProgressRecorder(self)
    try:
        Repo.clone_from(repo_link, abs_local_path, branch='master', depth=1)
        # progress_recorder.set_progress()
        success1 = f'Github link Cloned to {abs_local_path}'
        return 'Done'
    except git.GitCommandError:
        error1 = f"Bad Repo Link or Existing cloned Repo, Didn't clone {repo_link}"
        return 'Error Occured'
