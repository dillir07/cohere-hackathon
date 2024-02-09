import os
import json


def write_to_file(file_path: str, content: str | dict) -> None:
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as out:
        if isinstance(content, str):
            out.write(content)
        elif isinstance(content, dict):
            json.dump(content, out)


def read_file(file_path: str):
    try:
        with open(file_path, "r") as file:
            contents = file.read()
        return contents
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found at path: {file_path}") from None
    except IOError as e:
        raise IOError(f"Error reading file: {e}") from None


def read_json(file_path: str):
    if not file_path.lower().endswith(".json"):
        raise FileNotFoundError(f"{file_path} is not json file")
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found at path: {file_path}") from None
    except IOError as e:
        raise IOError(f"Error reading file: {e}") from None


def get_files_from_directory(directory: os.PathLike) -> list[str]:
    all_files: list[str] = []
    for root, dirs, files in os.walk(directory):
        all_files.extend(files)
    return all_files


def hashtagify(items: list[str]):
    hashtags: list[str] = []
    for item in items:
        words = item.split(" ")
        if len(words) > 3:
            continue
        capitalized = []
        for word in words:
            capitalized.append(word.capitalize())
        capitalized.insert(0, "#")
        hashtags.append("".join(capitalized))
    return hashtags
