def create_file(file_name: str) -> None:
    with open(f'{file_name}', 'w') as new_file:
        pass


def write_line_to_file(file_name: str, line: str) -> None:
    with open(f'{file_name}','a') as file:
        file.write(line)


def create_backup(path: str) -> None:
    file_name = path.split("\\")[-1]
    with open(f"{path}", 'r') as file:
        with open(f"{"backups" + "\\" + file_name}" 'w') as backup:
            backup.writelines(file.readlines())


def read_log(activity_log_file: str) -> list:
    with open(f"{activity_log_file}", 'r') as file:
        return file.readlines()
