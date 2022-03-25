from json import dumps
from sys import argv
from os import system, listdir
from os.path import join, isdir


class Jupyter:
    data = dict(
        topics=[
            i for i in listdir("./nbs")
            if i not in ["assets", "info.json", "run.py", "__pycache__"]
        ],
        content={}
    )
    
    def start(self):
        self.update()
        try:
            system("cd ./nbs && jupyter notebook")
        except KeyboardInterrupt:
            pass
            
    def get_topic(self, name):
        x, xdata = listdir(join("./nbs", name)), {}
        if x:
            for xi in x:
                xpath = join("./nbs", name, xi)
                if isdir(xpath):
                    xdata[xi] = {y: join("notebooks", name, xi, y) for y in listdir(xpath) if y.endswith(".ipynb")}
                elif xi.endswith(".ipynb"):
                    xdata[xi] = join("notebooks", name, xi)
        self.data["content"][name] = xdata
    
    def update(self):
        for i in self.data["topics"]:
            self.get_topic(i)            
        with open("info.json", "w") as f:
            f.write(dumps(
                self.data, 
                **dict(
                    indent=4,
                    sort_keys=True,
                    ensure_ascii=False
                )
            ))
            
    def git_push(self):
        self.update()
        system(
            " && ".join([
                "git add .", "git commit -m 'autocommit'"
            ])
        )
        system("git push")
                    
    
if __name__ == "__main__":
    args = argv[1:]
    if "update" in args:
        Jupyter().update()
    if "push" in args:
        Jupyter().git_push()
    if "jupyter" in args:
        Jupyter().start()

