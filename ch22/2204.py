import os


def two_files(filepath1, filepath2, output_path="data/combined.txt"):
    if not os.path.exists(filepath1) or not os.path.exists(filepath2):
        raise FileNotFoundError("One or more input files are missing")

    with open(filepath1, "r") as f1, open(filepath2, "r") as f2:
        file1 = f1.read()
        file2 = f2.read()

    with open(output_path, "w") as f3:
        f3.write(file1 + "\n" + file2)


if __name__ == "__main__":
    try:
        two_files("data/flatland01.txt", "data/IncidentTicket.txt")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except IOError as e:
        print(f"Error: Cannot write to location: {e}")