def write(path, data, mode="a"):
    if mode not in ["w","a"]:
        raise ValueError(f"Invalid mode '{mode}'. it should be 'w' or 'a'.")
    with open(path, mode) as f:
        f.write(data)

def read(path):
    try:
        with open(path, "r") as f:
            return f.read()
    except FileNotFoundError as _:
        return ""
