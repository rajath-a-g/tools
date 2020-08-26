import git
import os
from Evioconfig import COMMIT as evioconfig



class version:
    def __init__(self):
        self.evio_repo = None
        self.repo_tools = None

    def getrepository(self):
        """
        Print the active branch name of the Evio and Tools repo. If Multiple repos are found, What to do?
        More efficient way to do it has to be worked upon.
        """
        present_dir = os.getcwd()[0:3]
        print(present_dir)
        for root, subdirs, files in os.walk(present_dir):
            for d in subdirs:
                if d == "evio":
                    dir_path = os.path.join(root, d)

        self.evio_repo = git.Repo(dir_path)
        print("Evio Branch name:" + str(self.evio_repo.active_branch))
        for root, subdirs, files in os.walk(present_dir):
            for d in subdirs:
                if d == "tools":
                    dir_path_tools = os.path.join(root, d)
        self.repo_tools = git.Repo(dir_path_tools)
        print("Tools Branch name:" + str(self.repo_tools.active_branch))

    def sync(self):

        current_commit = self.evio_repo.active_branch.commit
        tools_commit = self.repo_tools.active_branch.commit
        if evioconfig[str(current_commit)] != tools_commit:
             print("Change commit")
        print(current_commit)
        print(tools_commit)

    def main(self):
        self.getrepository()
        self.sync()


if __name__ == "__main__":
    version = version()
    version.main()
