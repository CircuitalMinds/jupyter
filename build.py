from sys import argv
from os import system
from json import dumps
from libs.utils import base_path
jupyter_path = base_path.joinpath("application/jupyter")
folders = [
    i.name for i in jupyter_path.joinpath("nbs").iterdir()
    if i.name != "assets"
]


class Info:

    def __init__(self):
        self.file = jupyter_path.joinpath("dataset.json")
        self.data = dict(
            root="https://jupyternbs.herokuapp.com/notebooks",
            available_space=True,
            total_size=0.0,
            content=dict()
        )

    def save(self):
        self.file.open("w").write(dumps(
            self.data,
            indent=4,
            sort_keys=True,
            ensure_ascii=False
        ))


class Content:

    def __init__(self):
        self.info = Info()
        for name in folders:
            self.get_folder(name)
        self.info.save()

    def save(self):
        jupyter_path.joinpath("notebooks.json").open("w").write(
            dumps(
                self.info.data,
                indent=4,
                sort_keys=True,
                ensure_ascii=False
            )
        )

    def get_folder(self, name):
        self.info.data["content"][name] = dict()
        for module in jupyter_path.joinpath(f"nbs/{name}").iterdir():
            if module.name != ".ipynb_checkpoints":
                files = []
                for file in module.iterdir():
                    if file.name.endswith(".ipynb"):
                        files.append(dict(
                            name=file.name,
                            path=str(file.relative_to(jupyter_path.joinpath("nbs"))),
                            size=file.stat().st_size * 1.024e-6
                        ))
                self.info.data["total_size"] += sum(i["size"] for i in files)
                self.info.data["content"][name][module.name] = files


def run():
    system(f"cd {str(jupyter_path)} && bash run")


def push():
    system(f"cd {str(jupyter_path)} && bash push")


if __name__ == "__main__":
    Content()
    if "run" in argv:
        run()
    elif "push" in argv:
        push()
