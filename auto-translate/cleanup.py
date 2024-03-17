import os


def remove_user_files():
    for root, dirs, files in os.walk("patterns"):
        for file in files:
            if file.endswith('user.md'):
                os.remove(os.path.join(root, file))


def list_non_empty_user_files():
    for root, dirs, files in os.walk("patterns"):
        for file in files:
            if file.endswith('user.md'):
                file_path = os.path.join(root, file)
                if os.stat(file_path).st_size > 0:
                    print(file_path)


def cleanup():
    for root, dirs, files in os.walk("patterns"):
        for file in files:
            if file.endswith('_de.md'):
                os.remove(os.path.join(root, file))


remove_user_files()
list_non_empty_user_files()
cleanup()
