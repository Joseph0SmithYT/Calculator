class CustomTerminal():
    def __init__(self):
        self.commands = {"help": self.show_commands}
        self.command_line_prompt = "<root> $ "


    def show_commands(self):
        print(f'Help menu')
        for command in self.commands:
            print(f'- {command}')

    def register_command(self, command_name):
        def decorator(function_name):
            self.commands[command_name] = function_name
            return function_name
        return decorator
    
    def execute_command(self, command):
        if command in self.commands:
            self.commands[command]()
        else:
            print("Command wasn't found!")
            
    def start_terminal(self):
        while True:
            user_input = input(self.command_line_prompt)
            self.execute_command(user_input)


def main():
    terminal = CustomTerminal()
    terminal.show_commands()
    @terminal.register_command('custom')
    def custom_command():
        print("ermmm ur a nerd haha")

    while True:
        user_input = input('<root/home> $ ')
        terminal.execute_command(user_input)




if __name__ == "__main__":
    main()