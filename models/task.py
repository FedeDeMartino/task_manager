from enums.priority import Priority
import pdb

class Task:
  def __init__(self, name, priority = Priority.LOW):
    self.name = name
    self.completed = False
    self.priority = priority

  def complete(self):
    self.completed = True

  def edit(self, name, priority):
    self.name = name
    self.priority = priority

  def __str__(self):
    status = "✔" if self.completed else "✘"
    priority = "^^^" if int(self.priority) == Priority.HIGH.value else ("^^" if int(self.priority) == Priority.MEDIUM.value else "^")
    return f"[{status}] {self.name}, Priority: {priority}"
