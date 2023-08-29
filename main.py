
tasks = []

print("Welcome to your to-do list\n")

while True:

   print("\n1-Create a new task")
   print("2-Show all tasks")
   print("3-Clear all tasks")
   print("4-Delete a task")
   print("5-Quit")

   choose = input("Input here: ")

   if choose == "1":
      newTask = input("\nPlease enter your task's name: ")
      try:
         tasks.append(newTask)
         print("Task successfully created.")
      except:
         print("Task create failed. Please try again.")

   if choose == "2":
      print("")
      for i in range(0, len(tasks)):
         value = i + 1
         print(str(value) + "- " + tasks[i])

   if choose == "3":
      try:
         tasks = []
         print("\nAll tasks successfully cleaned.")
      except:
         print("Task clean failed. Please try again.")

   if choose == "4":
      print("")
      for i in range(0, len(tasks)):
         value = i + 1
         print(str(value) + "- " + tasks[i])
      deleteItem = input("\nPlease enter the number of the completed task: ")
      try:
         deleteItemValue = int(deleteItem) - 1
         tasks.remove(tasks[deleteItemValue])
         print("Task is successfully deleted.")
      except:
         print("Task delete failed. Please try again.")

   if choose == "5":
      break
   