class Task:
    def __init__(self, DateStart, DateFinish, Description):
        self.DateStart = DateStart
        self.DateFinish = DateFinish
        self.Description = Description
tasks = [
    Task("2025-05-01", "2025-05-10", "Задача1"),
    Task("2025-05-13", "2025-05-24", "Задача2"),
    Task("2025-04-23", "2025-05-02", "Задача3"),
    Task("2025-05-05", "2025-05-21", "Задача4"),
    Task("2025-04-29", "2025-05-16", "Задача5")
]
latest_task = None
for task in tasks:
    if latest_task is None or task.DateFinish > latest_task.DateFinish:
        latest_task = task
if latest_task:
    print(f"Занятие, заканчивающееся позже всех:\nДата начала: {latest_task.DateStart}\n"
          f"Дата окончания: {latest_task.DateFinish}\n{latest_task.Description}")
else:
    print("Список задач пуст")