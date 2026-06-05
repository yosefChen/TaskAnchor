def write_the_log(line: str) -> None:
    with open("activity_log.txt", 'a') as file:
        file.write(line + "\n")


def create_backup(path: str) -> None:
    file_name = path.split("\\")[-1]
    with open(f"{path}", 'r') as file:
        with open(f"{'backups\\' + file_name}", 'w') as backup:
            backup.writelines(file.readlines())


def read_log() -> list:
    with open(f"activity_log.txt", 'r') as file:
        return file.readlines()

