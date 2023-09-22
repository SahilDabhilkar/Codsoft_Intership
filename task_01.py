from tkinter import *
from tkinter import messagebox


def add_task():
    # Get the task from the entry field
    task = entry_1.get()
    
    if task:
        # Create the task text with an unchecked checkbox
        task_text = f"☐ {task}"  # Adding a Unicode checkbox character
        list_box.insert(END, task_text)
        entry_1.delete(0, END)
        messagebox.showinfo("Task Added", "Task added successfully!")

def delete_task():
    try:
        # Get the selected task's index and delete it
        task_index = list_box.curselection()[0]
        list_box.delete(task_index)
        messagebox.showinfo("Task Removed", "Task Removed Successfully")
    except IndexError:
        messagebox.showerror("Error", "No task selected for deletion")

def mark_as_done():
    try:
        # Get the selected task's index and text, then mark it as done with a checked checkbox
        task_index = list_box.curselection()[0]
        task_text = list_box.get(task_index)
        updated_task_text = task_text.replace("☐", "☑")  # Replace checkbox
        list_box.delete(task_index)
        list_box.insert(task_index, updated_task_text)
        messagebox.showinfo("Task Marked", "Task Marked As Done ")
    except IndexError:
        messagebox.showerror("Error", "No task selected to mark as done")


# Create the main window
root = Tk()
root.title("To-Do Lists")
root.geometry("800x500")

# Label for the title
head1 = Label(root, text="To-Do Lists", font=('Arial', 25))
head1.pack()

# List box to display tasks
list_box = Listbox(root, height=15, width=80, selectmode=SINGLE)
list_box.pack()

# Entry field for task input
entry_1 = Entry(root)
entry_1.pack()

# Buttons for adding, removing, marking as done, and saving
add_button = Button(root, text="Add Task", command=add_task, bg="lightblue", padx=10)
add_button.pack()

remove_button = Button(root, text="Remove Task", command=delete_task, bg="lightcoral", padx=10)
remove_button.pack()

done_button = Button(root, text="Mark as Done", command=mark_as_done, bg="lightgreen", padx=10)
done_button.pack()



# Start the Tkinter main loop
root.mainloop()
