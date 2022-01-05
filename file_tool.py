import csv, json


class FileTool:
    """represent a filetool"""

    def __init__(self, path, fields=[]):
        """Initialize attributes to describe filetool"""
        self.path = path
        self.fields = fields

    def program(self):
        options = self.menu_options()

        if options == 1:
            self.search()
        elif options == 2:
            self.add()
        elif options == 3:
            self.delete()
        elif options == 4:
            self.update()
        elif options == 5:
            self.open_file()
        elif options == 6:
            self.create_file()
        elif options == 7:
            self.csv_to_json()


    def open_file(self):
        csv.register_dialect('normal_reading', delimiter=',', quoting=csv.QUOTE_MINIMAL)
        """open_file() function look this file in the directory"""
        """the keyword 'with' closes the file once access to is no longer."""
        with open(self.path, mode='r', encoding='utf-8') as file_object:
            "read file via csv.reader() and it returns an iterator. "
            contents = csv.reader(file_object, dialect='normal_reading')
            for lines in contents:
                print(lines)

    def menu_options(self):
        options = int(input(
            "*** Please Enter a number between 1 and 8 ***\n\n1-Search\n2-Add\n3-Delete\n4-Update\n5-Open file\n6-Create a new file\n7-Csv to Json\n\nEnter your choice: "))
        while options < 1 or options > 7:
            options = int(input("Please Enter a number between 1 and 8: "))
        return options

    def add(self):
        """Add new input from user at the end of the text"""
        """newline default value is \n so we should replace with ''  """
        with open(self.path, 'a', newline='') as file:
            text = input("Please enter the text: ")
            writer = csv.writer(file, delimiter=',', quating=csv.QUOTE_ALL)
            writer.writerow(text)

    def delete(self):
        """Delete text from """
        # https://stackoverflow.com/questions/4710067/how-to-delete-a-specific-line-in-a-file
        text = input("Plese write the text you wanna delete: ")
        with open(self.path, mode='r') as file_input:
            lines = file_input.readlines()
        with open(self.path, 'w') as file_input:
            for line in lines:
                if line.strip("\n") != text:
                    file_input.write(line)

    def update(self):
        """Update text via user input"""
        text = input("Please enter the text you wanna update")
        new_text = input("Please enter the new text")
        newlines = []
        with open(self.path, mode='r') as file:
            list_of_lines = file.readlines()
            for line in list_of_lines():
                newlines.append(line.replace(text, new_text))
        with open(self.path, mode='w') as file:
            file.write(line)

    def search(self):
        """Search text"""
        text = input("Please enter the text you looking for")
        with open(self.path, mode='r') as file:
            list_of_lines = file.readlines()
            for line in list_of_lines:
                if text in line:
                    print(line)

    def csv_to_json(self):
        """Change as a json format"""
        with open(self.path, 'r') as csv_file:
            with open(self.path, 'w') as json_file:
                reader = csv.DictReader(csv_file, delattr(';'))
                json.dump(list(reader), json_file)

    def create_file(self):
        text = input("Please enter the file name you want to create")
        with open(self.path, mode='x') as file:
            file.write(text)



path_name = input("Write out a full path to clarify where you want FileTool to look: ")
FileTool(path_name).program()
