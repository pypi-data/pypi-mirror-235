import os
from pathlib import Path


class MdDB:
    def __init__(self, path: str = None) -> None:
        self.path = Path(path or os.getcwd()) / "mdb"
        self.path.mkdir(exist_ok=True)

    def create(self, dictionary: dict, filename: str, level: int = 1) -> str:
        md = self._dict_to_md(dictionary, level)
        try:
            (self.path / filename).write_text(md)
        except Exception as e:
            raise e
        return md

    def _dict_to_md(self, dictionary: dict, level: int) -> str:
        md = ""
        for key, value in dictionary.items():
            md += f"{level * '#'} {key}\n"
            if isinstance(value, dict):
                md += self._dict_to_md(value, level + 1)
            else:
                md += f"{value}\n"
        return md

    def read(self, filename: str) -> dict:
        md = (self.path / filename).read_text()
        return self._md_to_dict(md)

    def _md_to_dict(self, md: str) -> dict:
        lines = md.splitlines()
        output = {}
        stack = []
        for line in lines:
            line = line.strip()
            if not line:
                continue
            if line.startswith("#"):
                level = len(line) - len(line.lstrip("#"))
                key = line.lstrip("#").strip()
                if level == 1:
                    output[key] = {}
                    stack = [key]
                else:
                    while len(stack) > level - 1:
                        stack.pop()
                    parent = output
                    for k in stack:
                        parent = parent[k]
                    parent[key] = {}
                    stack.append(key)
            else:
                key = stack[-1]
                parent = output
                for k in stack[:-1]:
                    parent = parent[k]
                try:
                    value = int(line)
                except ValueError:
                    try:
                        value = float(line)
                    except ValueError:
                        value = self.parse_list(line)
                parent[key] = value

        return output

    def parse_list(self, line):
        try:
            items = line.split(",")
            kv = [item.split(" ") for item in items]
            if len(kv[0]) == 2:
                out = {item[0]: int(item[1]) for item in kv}
            else:
                out = kv[0][0]
        except ValueError:
            items = line.split(", ")
            kv = [item.split(" ") for item in items]
            if len(kv[0]) == 2:
                out = {item[0]: int(item[1]) for item in kv}
            else:
                out = kv[0][0]
        return out

    def delete(self, filename: str) -> None:
        file_path = self.path / filename
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"Deleted {filename}")
        else:
            print(f"The file {filename} does not exist")
