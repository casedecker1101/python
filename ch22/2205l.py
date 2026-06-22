def input_file(path="data/combined.txt"):
    try:
        with open(path, "r", encoding="utf-8") as f1:
            return f1.read()
    except FileNotFoundError:
        print(f"Error: file not found: {path}")
    except OSError as e:
        print(f"Error reading {path}: {e}")
    return None


def transform_file(text):
    if text is None:
        return None
    # Normalize whitespace and lowercase the content.
    return " ".join(text.split()).lower()


def write_file(text, path="data/fileConvert.txt"):
    if text is None:
        return False
    try:
        with open(path, "w", encoding="utf-8") as file_convert:
            file_convert.write(text)
        return True
    except OSError as e:
        print(f"Error writing {path}: {e}")
        return False


def main():
    content = input_file()
    transformed = transform_file(content)
    if write_file(transformed):
        print("Wrote data/fileConvert.txt")


if __name__ == "__main__":
    main()

