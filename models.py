class Task:
    def __init__(self, name, duration, predecessors):
        self.name = name
        self.duration = duration
        self.predecessors = predecessors
        self.faz = 0  # Frühester Anfangszeitpunkt
        self.fez = 0  # Frühester Endzeitpunkt
        self.saz = 0  # Spätester Anfangszeitpunkt
        self.sez = 0  # Spätester Endzeitpunkt
        self.gp = 0   # Gesamtpuffer
        self.fp = 0   # Freier Puffer

class NetworkPlan:
    def __init__(self, tasks):
        self.tasks = tasks

    def add_task(self, task):
        self.tasks.append(task)