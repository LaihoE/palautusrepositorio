from urllib import request
from project import Project
import tomli

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        content_str = request.urlopen(self._url).read().decode("utf-8")
        toml_dict = tomli.loads(content_str)
        # Don't need outer nest right now atleast
        toml_dict  = toml_dict["tool"]["poetry"]
        return Project(toml_dict["name"], toml_dict["description"], toml_dict["dependencies"], toml_dict["dev-dependencies"])
