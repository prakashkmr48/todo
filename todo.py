import streamlit as st
import sqlite3

def create_task_table(connection):
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY,
            task_name TEXT,
            completed INTEGER
        )
    ''')
    connection.commit()

def save_task(connection, task_name):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO tasks (task_name, completed) VALUES (?, ?)", (task_name, 0))
    connection.commit()

def load_tasks(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    return tasks

def update_task_completion(connection, task_id, completed):
    cursor = connection.cursor()
    cursor.execute("UPDATE tasks SET completed = ? WHERE id = ?", (completed, task_id))
    connection.commit()

def main():
    st.title("To-Do List App")
    connection = sqlite3.connect('tasks.db')
    create_task_table(connection)

    action = st.selectbox("Select an action:", ["View Tasks", "Add Task"])

    if action == "View Tasks":
        st.header("View Tasks")
        tasks = load_tasks(connection)
        if not tasks:
            st.write("No tasks available.")
        else:
            for task_id, task_name, completed in tasks:
                task_name_display = f"~~{task_name}~~" if completed else task_name
                completed_checkbox = st.checkbox("", value=completed, key=f"checkbox_{task_id}")
                st.write(f"{task_name_display}")
                if completed_checkbox != completed:
                    update_task_completion(connection, task_id, 1 if completed_checkbox else 0)
                    st.success("Task status updated successfully.")

    elif action == "Add Task":
        st.header("Add Task")
        task_name = st.text_input("Enter task:")
        if st.button("Add"):
            if task_name:
                save_task(connection, task_name)
                st.success("Task added successfully!")

    connection.close()

if __name__ == "__main__":
    main()
