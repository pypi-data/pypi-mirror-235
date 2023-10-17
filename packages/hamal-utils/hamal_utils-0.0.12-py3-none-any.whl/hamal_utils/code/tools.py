from subprocess import run


def get_version():
    tags = run(["git", "describe", "--tags"], capture_output=True, text=True)
    tags = tags.stdout.strip()
    tag = tags.split("\n")[-1]
    version = tag.split("-")[-1]
    return version
