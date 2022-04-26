from json import dumps
from sys import argv
from os import system, listdir
from os.path import join, isdir


class Jupyter:
    path = "./nbs"
    topics = ("Intro", "Engineering", "ScienceData")

    def __init__(self):
        self.data = dict()
        self.get_data()

    def get_data(self):
        for i in self.topics:
            self.data[i] = {}
            for j in listdir(join(self.path, i)):
                fpath = join(self.path, i, j)
                if isdir(fpath):
                    self.data[i][j] = {}
                    for f in filter(lambda x: x.endswith(".ipynb"), listdir(fpath)):
                        self.data[i][j][f] = join("notebooks", i, j, f)
                elif j.endswith(".ipynb"):
                    self.data[i][j] = join("notebooks", i, j)

    def save_info(self):
        with open("info.json", "w") as f:
            f.write(dumps(
                self.data, **dict(
                    indent=4, sort_keys=True, ensure_ascii=False
                )
            ))

    def update(self):
        self.get_data()
        self.save_info()
        system("bash push.sh")

    def run(self):
        self.update()
        try:
            system("cd ./nbs && jupyter notebook")
        except KeyboardInterrupt:
            pass


if __name__ == "__main__":
    args = argv[1:]
    if "jupyter" in args:
        Jupyter().run()
    if "update" in args:
        Jupyter().update()

