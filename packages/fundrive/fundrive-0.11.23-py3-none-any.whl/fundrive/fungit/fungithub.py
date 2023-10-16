import json
import logging
import subprocess
from typing import Any

from fundrive.core import DriveSystem
from funsecret import read_secret

logger = logging.getLogger("farfarfun")


class GithubDrive(DriveSystem):
    def __init__(self, *args, **kwargs):
        super(GithubDrive, self).__init__(*args, **kwargs)
        self.repo = None

    def login(self, repo_str, access_tokens=None, *args, **kwargs) -> bool:
        try:
            from github import Github
        except Exception as e:
            subprocess.check_call(["pip", "install", "pygithub"])
            from github import Github

        if access_tokens:
            read_secret(cate1="github", cate2="access_tokens", cate3="pygithub", value=access_tokens)
        else:
            access_tokens = read_secret(cate1="github", cate2="access_tokens", cate3="pygithub")
        self.repo = Github(access_tokens).get_repo(repo_str)
        return True

    def get_dir_info(self, git_path, *args, **kwargs) -> dict[str, Any]:
        data = self.get_dir_list(git_path)
        if len(data) > 0:
            return data[0]
        return {}

    def get_file_info(self, git_path, *args, **kwargs) -> dict[str, Any]:
        data = self.get_file_list(git_path)
        if len(data) > 0:
            return data[0]
        return {}

    def get_file_list(self, git_path, recursive=False, *args, **kwargs) -> list[dict[str, Any]]:
        all_files = []
        try:
            contents = self.repo.get_contents(git_path)
            if not isinstance(contents, list):
                contents = [contents]
        except Exception as e:
            contents = []
        while contents:
            file_content = contents.pop(0)
            if file_content.type != "dir":
                all_files.append({"name": file_content.name, "path": file_content.path, "size": file_content.size})
            elif recursive:
                contents.extend(self.repo.get_contents(file_content.path))
        return all_files

    def get_dir_list(self, git_path, recursive=False, *args, **kwargs) -> list[dict[str, Any]]:
        all_files = []
        try:
            contents = self.repo.get_contents(git_path)
            if not isinstance(contents, list):
                contents = [contents]
        except Exception as e:
            contents = []
        while contents:
            file_content = contents.pop(0)
            if file_content.type == "dir":
                all_files.append({"name": file_content.name, "path": file_content.path, "size": file_content.size})
                if recursive:
                    contents.extend(self.repo.get_contents(file_content.path))
        return all_files

    def upload_file(
        self,
        file_path="./cache",
        content=None,
        git_path=None,
        message="committing files",
        branch="master",
        overwrite=False,
        *args,
        **kwargs,
    ) -> bool:
        if content is None:
            content = open(file_path, "r").read()
        if not isinstance(content, str):
            content = json.dumps(content)
        if len(self.get_file_list(git_path=git_path)) > 0:
            contents = self.repo.get_contents(git_path)
            self.repo.update_file(contents.path, message, content, contents.sha, branch=branch)
            logger.info(f"{git_path} UPDATED")
        else:
            self.repo.create_file(git_path, message, content, branch=branch)
            logger.info(f"{git_path} CREATED")
        return True
