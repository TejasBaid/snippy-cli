from .app import Snipper
import sys
from .interactive_mode import interactive_mode

def main():
    snipper = Snipper()
    args = sys.argv[1:]

    if not args:
        # If no arguments are provided, show help
        print("⚠️  No command provided. Use 'help' for usage information.\n")
        snipper.help()
        return

    command = args[0].lower()  # Command is the first argument

    # Dictionary mapping commands to Snipper methods
    command_map = {
        "create": snipper.make_snip,
        "make": snipper.make_snip,
        "show": snipper.list,
        "list": snipper.list,
        "open": snipper.open,
        "copy": snipper.copy,
        "cp": snipper.copy,
        "delete": snipper.delete,
        "remove": snipper.delete,
        "rm": snipper.delete,
        "help": snipper.help,
        "--help": snipper.help,
        "interactive": interactive_mode  # Add interactive mode support
    }

    # If the command exists in the map, call the corresponding function
    if command in command_map:
        try:
            if command in ["create", "make", "open", "copy", "delete", "remove", "rm"]:
                # Commands that require an additional argument (snippet name)
                if len(args) < 2:
                    print(f"❌ Missing argument for '{command}' command. Please specify the snippet name.\n")
                    return
                command_map[command](args[1])
            else:
                # Commands that don't need additional arguments (like list and help)
                command_map[command]()
        except Exception as e:
            print(f"❌ An error occurred while executing the '{command}' command: {e}\n")
    else:
        # If the command is not recognized, show an error and display help
        print(f"❌ Unknown command: '{command}'. Use 'help' for available commands.\n")
        snipper.help()

if __name__ == '__main__':
    main()
