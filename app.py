from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data
initiatives = [
    {'id': 1, 'title': 'Tree Planting Campaign', 'description': 'Join us in planting trees in our community park.'},
    {'id': 2, 'title': 'Beach Cleanup', 'description': 'Help us clean up the beach and protect marine life.'},
    {'id': 3, 'title': 'Recycling Drive', 'description': 'Participate in our recycling drive to reduce waste.'}
]
next_id = 4

@app.route('/')
def index():
    return render_template('index.html', initiatives=initiatives)

@app.route('/add', methods=['GET', 'POST'])
def add():
    global next_id
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        initiatives.append({'id': next_id, 'title': title, 'description': description})
        next_id += 1
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/delete/<int:id>')
def delete(id):
    global initiatives
    initiatives = [initiative for initiative in initiatives if initiative['id'] != id]
    return redirect(url_for('index'))

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    initiative = next((initiative for initiative in initiatives if initiative['id'] == id), None)
    if request.method == 'POST':
        initiative['title'] = request.form['title']
        initiative['description'] = request.form['description']
        return redirect(url_for('index'))
    return render_template('edit.html', initiative=initiative)

if __name__ == '__main__':
    app.run(debug=True, port=8080)
