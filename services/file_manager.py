class FileManager:
  def __init__(self, filename='./data/tasks.txt'):
    self.filename = filename

  def create(self, tasks):
    with open(self.filename, "w") as file:
      for task in tasks:
        file.write(f"{task.name},{task.completed},{task.priority}\n")
  
  def load(self):
    try:
      tasks = []
      with open(self.filename, "r") as file:
        for line in file:
          name, completed, priority = line.strip().split(",")
          tasks.append((name, completed, priority))
      return tasks
    except FileNotFoundError:
      print("No tasks saved")

  def save(self, tasks):
    self.remove_all()
    self.create(tasks)

  def remove_all(self):
    try:
      with open(self.filename, "w") as file:
        file.write("")
    except FileNotFoundError:
      print("No tasks removed")
