import os.path

from fundrive import GithubDrive


class Result:
    def __init__(self):
        self.drive = GithubDrive()
        self.drive.login("farfarfun/funread-cache")

    def book(self, dir_path="funread/legado/snapshot/lasted/book"):
        files = self.drive.get_file_list(dir_path)
        files = sorted(files, key=lambda x: x["time"])
        return {
            "title": os.path.basename(dir_path),
            "time": files[0]["time"],
            "pic": "https://gitee.com/alanskycn/yuedu/raw/master/JS/icon.jpg",
            "url": f"https://farfarfun.github.io/funread-cache/{dir_path}/index.html",
            "content": "this is content",
        }

    def generate(self, dir_path="funread/legado/snapshot/lasted"):
        data1 = {
            "name": "test",
            "next": "https://json.extendsclass.com/bin/b62da68f7d4d",
            "list": [],
        }
        data1["list"].append(self.book(f"{dir_path}/book"))
        self.drive.upload_file(git_path=f"{dir_path}/source.json", content=data1)


Result().generate()
