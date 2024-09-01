def find_task_by_name(network_plan, name):
    for task in network_plan.tasks:
        if task.name == name:
            return task
    return None

def calculate_schedule(network_plan):
    # FAZ und FEZ Berechnung (Vorwärtsplanung)
    for task in network_plan.tasks:
        if task.predecessors:
            predecessor_end_times = [
                find_task_by_name(network_plan, p).fez 
                for p in task.predecessors 
                if find_task_by_name(network_plan, p) is not None
            ]
            if predecessor_end_times:
                task.faz = max(predecessor_end_times)
            else:
                task.faz = 0
        task.fez = task.faz + task.duration
    
    # SEZ und SAZ Berechnung (Rückwärtsplanung)
    max_end_time = max(task.fez for task in network_plan.tasks)
    for task in reversed(network_plan.tasks):
        if task.predecessors:
            predecessor_start_times = [
                find_task_by_name(network_plan, p).saz 
                for p in task.predecessors 
                if find_task_by_name(network_plan, p) is not None
            ]
            if predecessor_start_times:
                task.sez = min(predecessor_start_times)
            else:
                task.sez = max_end_time
        else:
            task.sez = max_end_time
        task.saz = task.sez - task.duration
        task.gp = task.sez - task.fez
        
        if task.predecessors:
            predecessor_faz_times = [
                find_task_by_name(network_plan, p).faz 
                for p in task.predecessors 
                if find_task_by_name(network_plan, p) is not None
            ]
            if predecessor_faz_times:
                task.fp = min(predecessor_faz_times) - task.fez
            else:
                task.fp = task.gp
        else:
            task.fp = task.gp
    
    # Kritischer Pfad Berechnung
    network_plan.critical_path = [task.name for task in network_plan.tasks if task.gp == 0]