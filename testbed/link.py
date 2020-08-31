import git
import os
import subprocess

from file_mappings import MAPPING as mapping


class link:
    def __init__(self):
        self.evio_repo = None
        self.tools_repo = None
        self.dir_path = None

    def sync(self):
        self.get_repository()
        process = subprocess.Popen("git describe --tags --abbrev=0", stdout=subprocess.PIPE, cwd=self.dir_path)
        output = process.communicate()[0].decode('ascii').strip()
        file_to_link = mapping[output[1:]]
        print(file_to_link)
        os.symlink(file_to_link, "./evt")

    def get_repository(self):
        """
        Get the active branch name of the Evio and Tools repo. If Multiple repos are found, What to do?
        More efficient way to do it has to be worked upon.
        """
        present_dir = os.getcwd()[0:3]
        print(present_dir)
        for root, subdirs, files in os.walk(present_dir):
            for d in subdirs:
                if d == "evio":
                    self.dir_path = os.path.join(root, d)

        self.evio_repo = git.Repo(self.dir_path)
        print("Evio Branch name:" + str(self.evio_repo.active_branch))
        for root, subdirs, files in os.walk(present_dir):
            for d in subdirs:
                if d == "tools":
                    dir_path_tools = os.path.join(root, d)
        self.tools_repo = git.Repo(dir_path_tools)
        print("Tools Branch name:" + str(self.tools_repo.active_branch))

    def main(self):
        self.sync()


if __name__ == "__main__":
    link = link()
    link.main()
