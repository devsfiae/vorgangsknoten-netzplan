from flask import Flask, render_template, request, redirect, url_for
from models import Task, NetworkPlan
from utils import calculate_schedule

app = Flask(__name__)

# Dummy data für Beispiel
tasks = [
    Task("A", 3, []),
    Task("B", 2, ["A"]),
    Task("C", 4, ["A"]),
    Task("D", 1, ["B", "C"])
]

network_plan = NetworkPlan(tasks)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        duration = int(request.form.get('duration'))
        predecessors = request.form.get('predecessors').split(',')
        new_task = Task(name, duration, predecessors)
        network_plan.add_task(new_task)
        return redirect(url_for('index'))
    
    # Berechnungen durchführen
    calculate_schedule(network_plan)
    
    return render_template('index.html', network_plan=network_plan)

if __name__ == '__main__':
    app.run(debug=True)