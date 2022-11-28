class todo:
    def __init__(self,name,priority):
        self.name =  name
        self.priority = priority
        self.status = "pending"
    
    def setpriority(self,val):
        self.priority = val
    
    def setstatus(self,val):
        self.status = val
    
    def setname(self,val):
        self.name=val
    
    def getpriority(self):
       return self.priority 

    def getstatus(self):
       return self.status
    
    def getname(self):
       return self.name 

import os

if os.path.exists('todo.txt'):
    with open('todo.txt', 'r') as f:
        b = f.read()
        tasks = eval(b) if len(b) > 0 else {}
else:
    a = open('todo.txt', 'a')
    a.close()
    tasks = {}


def addtask(name,priority):
    if name in tasks:
        print('task already present')
    elif name.strip() == ' ':
        print('taskname cant be empty')
    else:
        task = todo(name,priority)
        tasks[task.name]=[task.name,task.priority,task.status]
        print('task successfully added')
        with open('todo.txt', 'w') as f:
            f.write(str(tasks))
        

def edit_name(task, name):
    if task in tasks:
        if name in task.split(' '):
            print("Task already present")
            return
        else:
            # print(tasks[task])
            tasks[name] = tasks[task]
            tasks[name][0] = name
            del tasks[task]
            print("\ntask name updated\n")
    else:
        print("Task not found")
    with open('todo.txt', 'w') as f:
        f.write(str(tasks))
        f.close()
        


def edit_priority(task, priority):
    if task in tasks:
        if priority == tasks[task][1]:
            print("No Change in priority")
            return
        tasks[task][1] = priority
    else:
        print("Task not found")
    with open('todo.txt', 'w') as f:
        f.write(str(tasks))
        f.close()
        print("\nTask priority edited Succesfully!")


def edit_status(task, status):
    if task in tasks:
        if status == tasks[task][2]:
            print("No Change in status")
            return
        tasks[task][2] = status
    else:
        print("Task not found")
    with open('todo.txt', 'w') as f:
        f.write(str(tasks))
        f.close()
        print("Task status updated Succesfully!")


def delete(task):
    try:
        del tasks[task]
    except KeyError:
        print('Oops..! Task not Found')

    with open('todo.txt', 'w') as f:
        f.write(str(tasks))
        f.close()
        print("Task Deleted Succesfully!")


def search(task):
    print("\n{:<40} {:<40} {:<40}".format('Task', 'Priority', 'Status'))
    print('---------------------------------------------------------------------------------------------------------')
    toshow = None
    for key in tasks.keys():
        if task in key.split(' ') or task == key:
            toshow = key
            Task, Priority, Status = tasks[key]
            print("{:<40} {:<40} {:<40}".format(Task, Priority, Status))
    if toshow == None:
        print("\nOops..! No tasks with the keyword entered\n")


def show():
    print("\nHere are all the tasks: \n--------------------------------------------------------------------------------------------------\n")
    print("{:<40} {:<40} {:<40}".format('Task', 'Priority', 'Status'))
    print('---------------------------------------------------------------------------------------------------------')
    if tasks == {}:
        print("There are no tasks")
    else:
        
        for  value in tasks.values():
            Task, Priority, Status = value
            print("{:<40} {:<40} {:<40}".format(Task, Priority, Status))


def check(task):
    if task in tasks:
        return True
    else:
        return False

def clear(): return os.system('cls')  

import os,sys 
def main():
    option = 0
    while option != 7:
        print('\nMenu')
        print('----------------')
        print('1. Add a new todo Item \n')
        print('2. Delete a todo Item \n')
        print('3. Edit a todo Item \n')
        print('4. View all tasks \n')
        print('5. Search for a task \n')
        print('6. Exit \n')
        option = input('Enter your choice: ')

        if not option.isdigit():
            print('Please enter a valid option')
            input('Press enter to continue')
            clear()
        elif int(option) == 1:
            clear()
            print("Addition of a new task\n----------------")
            task = input('Enter Task name: ')
            if check(task):
                print("Task already present")
            else:
                priority = input('Enter the priority [High/Low/Medium]: ')
                if priority.lower() not in ['high', 'low', 'medium']:
                    print("Invalid Priority Entered!")
                    input("Press Enter to continue...")
                else:
                    addtask(task, priority)
                    input("Press Enter to continue...")
            clear()

        elif int(option) == 2:
            clear()
            print("Deletion of a task\n----------------")
            task = input('Enter Task name: ')
            if check(task):
                delete(task)
            else:
                print("Task not found")
            input("Press Enter to continue...")
            clear()

        elif int(option) == 3:
            clear()
            print("Editing of a task\n----------------")
            task = input('Enter Task name: ')
            while task not in tasks:
                task = input('No such Tasks to continue searching Enter Task name to return to main menu enter back \n')
                if task == 'back':
                    break
            if check(task):
                print("What do you want to edit? \n")
                print("1. Edit name \n")
                print("2. Edit priority \n")
                print("3. Edit status \n")
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    name = input("Enter new name: ")
                    edit_name(task, name)
                    input("Press Enter to continue...")
                elif choice == 2:
                    priority = input("Enter new priority [High/Low/Medium]: ")
                    while  priority.lower() not in ['high', 'low', 'medium']:
                        priority = input("Invalid new priority entered. Please choose a priority from the given options[High/Low/Medium]: ")
                    edit_priority(task, priority)
                    input("Press Enter to continue...")
                elif choice == 3:
                    status = input("Enter new status [Pending/Completed]: ")
                    while status.lower() not in ['completed','pending']:
                        status = input("Enter a Valid new status [Pending/Completed]: ")
                    edit_status(task, status)
                    input("Press Enter to continue...")
                else:
                    print("Invalid choice")

            else:
                input("\nPress Enter to continue...")
            clear()

        elif int(option) == 4:
            clear()
            show()
            input("\nPress Enter to continue...")
            clear()

        elif int(option) == 5:
            clear()
            print("Searching for a task\n----------------")
            task = input('Enter a keyword: ')
            search(task)
            input("\nPress Enter to continue...")
            clear()

        elif int(option) == 6:
            print("Goodbye!")
            sys.exit(0)
        
        else:
            print("Invalid choice!")
            input("\nPress Enter to continue...")
            clear()


if __name__ == "__main__":
    main()