
class Tasks:
    todo_list = {}
    descriptions = {}
    todo_list_items = {}
    def create_task(self, title, descr):
        width = str(len(self.todo_list) + 1)
        self.todo_list[width] = title
        self.descriptions[width] = descr
        return "created"

    def delete_task(self):
        pass

    def delete_task_items(self):

        pass

    def add_item2_task(self, task_title):
        pass
        
    def add_task_item(self,title):
        items_list = []
        print(self.todo_list_items)
        print("Add items to List Created!\n Add item and enter 1 when done")
        print("1. Done adding items")
        select = input("Input: ")
        if select == '1':
            return "done"
        elif select == "":
            print("Please enter valid data")
            self.add_task_item(title)
        elif title in self.todo_list_items and select not in self.todo_list_items[title]:
            items_list = self.todo_list_items[title]
            items_list.append(select)
            self.todo_list_items[title] = items_list
            self.add_task_item(title)
        if title in self.todo_list_items and select in self.todo_list_items[title]:
            print("Item already exists in the list")
            self.add_task_item(title)
        else:
            items_list.append(select)
            self.todo_list_items[title] = items_list
            self.add_task_item(title)

    def list_todos(self):
        pass

    def list_todo_items(self):
        pass

    