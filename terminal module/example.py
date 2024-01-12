import terminal

terminal = terminal.CustomTerminal()


terminal.command_line_prompt = "[SUDO] <root/home/i-386> $ "
@terminal.register_command('exit')
def exit():
    exit()


terminal.start_terminal()