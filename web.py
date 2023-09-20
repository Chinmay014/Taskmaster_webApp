import streamlit
import functions

tasks = functions.read_file()

def add_task():
    new_task = streamlit.session_state["new_task"]+"\n"
    tasks.append(new_task)
    functions.write_to_file(tasks)

streamlit.title("Taskmaster")
streamlit.write("Be the Taskmaster as you list and execute your tasks ;)")


for index,task in enumerate(tasks):
    checkbox = streamlit.checkbox(task,key=task)
    if checkbox:
        tasks.pop(index)
        functions.write_to_file(tasks)
        del streamlit.session_state[task]
        streamlit.experimental_rerun()
    # if streamlit.session_state[task]:
    #     tasks.remove(task)
    #     functions.write_to_file(tasks)
    #     del streamlit.session_state[task]
    #     streamlit.experimental_rerun()



streamlit.text_input(label="add task",placeholder="add your task here...", on_change=add_task, key="new_task",label_visibility="hidden") 