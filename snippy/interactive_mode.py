import sys
from .app import Snipper

def interactive_mode():
    snipper = Snipper()

    while True:
        # Display the interactive menu
        print("\nWelcome to Snippy Interactive Mode!")
        print("-------------------------------------")
        print("Choose an action:")
        print("1. Create a new snippet")
        print("2. List all snippets")
        print("3. Open a snippet for editing")
        print("4. Copy a snippet to clipboard")
        print("5. Delete a snippet")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == "1":
            snippet_name = input("Please enter the snippet name: ").strip()
            snipper.make_snip(snippet_name)
        elif choice == "2":
            snipper.list()
        elif choice == "3":
            snippet_name = input("Please enter the snippet name to open: ").strip()
            snipper.open(snippet_name)
        elif choice == "4":
            snippet_name = input("Please enter the snippet name to copy: ").strip()
            snipper.copy(snippet_name)
        elif choice == "5":
            snippet_name = input("Please enter the snippet name to delete: ").strip()
            snipper.delete(snippet_name)
        elif choice == "6":
            print("Exiting Snippy Interactive Mode. Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please select a valid option.")

def main():
    args = sys.argv[1:]

    if len(args) > 0 and args[0].lower() == "interactive":
        interactive_mode()
    else:
        # Handle non-interactive commands here (as per the original CLI logic)
        # For example, you can run help or specific commands like 'create', 'list', etc.
        pass

if __name__ == '__main__':
    main()
