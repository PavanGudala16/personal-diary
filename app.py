from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
DIARY_FILE = 'diary.txt'

def read_entries():
    if not os.path.exists(DIARY_FILE):
        return []
    with open(DIARY_FILE, 'r') as file:
        return file.readlines()

def write_entry(entry):
    with open(DIARY_FILE, 'a') as file:
        file.write(entry + '\n')

def delete_entry(index):
    entries = read_entries()
    if 0 <= index < len(entries):
        entries.pop(index)
        with open(DIARY_FILE, 'w') as file:
            file.writelines(entries)

@app.route('/')
def index():
    entries = read_entries()
    return render_template('index.html', entries=entries)

@app.route('/add', methods=['POST'])
def add_entry():
    entry = request.form['entry']
    if entry:
        write_entry(entry)
    return redirect(url_for('index'))

@app.route('/delete/<int:index>')
def delete_entry_route(index):
    delete_entry(index)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
