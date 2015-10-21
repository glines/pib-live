import gitrepobrowser

class BuildBrowser:
    def __init__(self, git_repo_path, patchwork_url, patchwork_project):
        self._git_repo_browser = gitrepobrowser.GitRepoBrowser(repo_path=git_repo_path)
        # TODO: Combine the git repo browser and patch browser trees
        self.widget = self._git_repo_browser.main_widget
        # TODO: Implement a patchwork browser
#        this._patchwork_browser = PatchworkBrowser(
#            url=patchwork_url, project=patchwork_project)
        pass
