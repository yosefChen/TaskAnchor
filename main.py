from models import Task
from utils import file_manager as utils
from time import sleep

def show_menu() -> None:
    print('~~~~~~~~~~~~~~~~~~~~~~~~')
    print('Welcome to TaskAnchor!!!')
    print('~~~~~~~~~~~~~~~~~~~~~~~~')
    print()
    print()
    print('Please choose from those options:')
    print('1) Document new task and backup it')
    print('2) Show document history')
    print('3) Exit')


def get_new_task_details() -> dict:
    input_dict = {"task_id": '', "developer": '', "description": '', "file_path": ''}
    for detail in input_dict:
        input_dict[detail] = input(f'Please enter the task detail - {detail}: ')
    return input_dict


def create_task(details: dict) -> str:
    new_task = Task(**details)
    return new_task.to_string()


def register_new_task() -> tuple:
    task_info = get_new_task_details()
    info_str = create_task(task_info)
    return info_str, task_info['file_path']


def write_log_info(info: str) -> None:
    utils.write_the_log(info)


def execute_action(action: str):
    if action == 'new':
        backup_file_info, file_path = register_new_task()
        write_log_info(backup_file_info)
        utils.create_backup(file_path)
        print('The file has been copied successfully, and has been added to the log!')
    elif action == 'show':
        print(utils.read_log())
    else:
        print('The program in closing down')
        print('Dont turn off the computer')
        sleep(3)
        print('The program will be shut down now')


def get_user_action() -> str:
    while True:
        action = input('Please choose (new / show / exit: ')
        if action.lower() == "new":
            return "new"
        elif action.lower() == "show":
            return "show"
        elif action.lower() == "exit":
            return "exit"


def main() -> None:
    action = ''
    show_menu()
    while action != 'exit':
        action = get_user_action()
        execute_action(action)


if __name__ == "__main__":
    main()
