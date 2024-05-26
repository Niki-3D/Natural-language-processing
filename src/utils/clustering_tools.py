@staticmethod
def split_name(name):
    parts = name.split()
    return (parts[0], parts[1]) if len(parts) == 2 else (name, '')