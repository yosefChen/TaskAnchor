class Task:
    def __init__(self, task_id: int, developer: str, description: str, file_path: str):
        self.task_id = task_id
        self.developer = developer
        self.description = description
        self.file_path = file_path


    def to_string(self) -> str:
        return f'{self.task_id}|{self.developer}|{self.description}|{self.file_path}'


