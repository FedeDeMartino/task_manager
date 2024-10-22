from models.task import Task
from services.file_manager import FileManager
import pdb

class TaskManager:
  def __init__(self):
    self.tasks = []

  def add(self, name, priority):
    priority = int(priority)
    task = Task(name, priority)
    self.tasks.append(task)
    self.save()

  def list_tasks(self):
    if not self.tasks:
      print("No tasks found.")
      return
    for idx, task in enumerate(self.tasks, 1):
      print(f"{idx}. {task}")

  def complete(self, task_number):
    if 0 < task_number <= len(self.tasks):
      self.tasks[task_number - 1].complete()
    else:
      print("Invalid task number")
  
  def edit(self, task_number, name, priority):
    if 0 < task_number <= len(self.tasks):
      self.tasks[task_number - 1].edit(name, priority)
    else:
      print("Invalid task number")
  
  def save(self):
    FileManager().save(self.tasks)
  
  def create(self):
    FileManager().create(self.tasks)

  def remove_all(self):
    FileManager().remove_all()

  def load(self):
    db_tasks = FileManager().load()
    self.tasks = []
    for task in db_tasks:
      name, completed, priority = task
      task = Task(name, priority)
      if completed == "True":
        task.complete()
      self.tasks.append(task)
