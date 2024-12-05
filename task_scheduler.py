import datetime

class TaskScheduler:
    def __init__(self):
        # The tasks will be stored in a dictionary with dates as keys and lists of tasks as values.
        self.tasks = {}

    def add_task(self, date, task_description):
        """Add a task for a specific date."""
        if date not in self.tasks:
            self.tasks[date] = []
        self.tasks[date].append(task_description)

    def view_tasks(self, date):
        """View tasks for a specific date."""
        return self.tasks.get(date, [])

    def delete_task(self, date, task_description):
        """Delete a specific task on a specific date."""
        if date in self.tasks and task_description in self.tasks[date]:
            self.tasks[date].remove(task_description)
            if not self.tasks[date]:
                del self.tasks[date]

    def list_all_tasks(self):
        """List all tasks."""
        return self.tasks

# Example usage:
if __name__ == "__main__":
    scheduler = TaskScheduler()

    # Add tasks
    scheduler.add_task("2023-09-15", "Doctor's appointment at 10 AM.")
    scheduler.add_task("2023-09-15", "Meeting with team at 3 PM.")
    scheduler.add_task("2023-09-16", "Submit project report.")

    # View tasks for a specific date
    print(scheduler.view_tasks("2023-09-15"))

    # Delete a task
    scheduler.delete_task("2023-09-15", "Doctor's appointment at 10 AM.")

    # List all tasks
    print(scheduler.list_all_tasks())
