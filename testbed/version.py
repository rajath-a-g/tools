import git
import os


class version:
    @staticmethod
    def getrepository():
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

        evio_repo = git.Repo(dir_path)
        print("Evio Branch name:" + str(evio_repo.active_branch))
        for root, subdirs, files in os.walk(present_dir):
            for d in subdirs:
                if d == "tools":
                    dir_path_tools = os.path.join(root, d)
        repo_tools = git.Repo(dir_path_tools)
        print("Tools Branch name:" + str(repo_tools.active_branch))


    def main(self):
        self.getrepository()


if __name__ == "__main__":
    version = version()
    version.main()
