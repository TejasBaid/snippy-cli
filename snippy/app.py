import sys
import tempfile
import os
import pyperclip
import editor
import subprocess  # To handle fallback case where editor.edit() fails
from os.path import isfile, join
from os import listdir



rootDir = os.path.dirname(__file__)
snippetDir = os.path.join(rootDir, "Snippets")


class Snipper:

    def create_dir(self):
        """Creates the Snippets directory if it doesn't exist."""
        if not os.path.exists(snippetDir):
            os.mkdir(snippetDir)
            print("📁 Created Snippets directory.\n")

    def list(self):
        """Lists all snippets in the Snippets directory in a tabular format."""
        self.create_dir()  # Ensure the Snippets directory exists

        onlyfiles = [f for f in listdir(snippetDir)]  # Get the list of snippets
        if onlyfiles:
            print("💡 Snippets in the directory:")
            print("=" * 40)

            # Calculate the longest snippet name for formatting
            max_length = max(len(f) for f in onlyfiles)
            header = f"{'#':<5} {'Snippet Name':<{max_length}}"
            print(header)
            print("-" * (5 + max_length + 2))

            # Display each snippet with its index in a formatted manner
            for index, filename in enumerate(onlyfiles):
                print(f"{index + 1:<5} {filename:<{max_length}}")

            print("=" * 40)
        else:
            print("⚠️  No snippets found in the directory.\n")

    def make_snip(self, name):
        """Creates a new snippet by opening an editor."""
        # Ensure the Snippets directory exists
        self.create_dir()

        # Open the editor to write a new snippet
        code_snippet = editor.editor()

        # Save the snippet
        snippet_path = os.path.join(snippetDir, name)
        with open(snippet_path, "a") as f:
            f.write(code_snippet)

        print(f"✅ Snippet '{name}' created successfully!\n")

    def open(self, name):
        """Opens an existing snippet for editing."""
        snippet_path = os.path.join(snippetDir, name)
        if not os.path.exists(snippet_path):
            print("❌ The snippet does not exist.\n")
        else:
            with open(snippet_path, "r+") as file:
                contents = file.read()

            # Open editor for editing the snippet
            updated_contents = editor.editor(contents=contents).decode("utf-8")

            # Optionally write updated contents back to the file
            with open(snippet_path, "w") as file:
                file.write(updated_contents)

            print(f"✏️  Snippet '{name}' updated successfully!\n")

    def copy(self, name):
        """Copies the content of a snippet to the clipboard."""
        snippet_path = os.path.join(snippetDir, name)
        if not os.path.exists(snippet_path):
            print("❌ The snippet does not exist.\n")
        else:
            with open(snippet_path, "r") as file:
                pyperclip.copy(file.read())

            print(f"📋 Snippet '{name}' copied to clipboard.\n")

    def delete(self, name):
        """Deletes a snippet from the Snippets directory."""
        snippet_path = os.path.join(snippetDir, name)
        if not os.path.exists(snippet_path):
            print("❌ The snippet does not exist.\n")
        else:
            os.remove(snippet_path)
            print(f"🗑️  Snippet '{name}' deleted successfully.\n")

    def help(self):
        """Displays available commands and their descriptions."""
        print("\n📖 Available Commands:")
        print("=" * 40)
        print("🛠️  create <name>:       Create a new snippet")
        print("📂 list:                List all snippets")
        print("✏️  open <name>:        Open a snippet for editing")
        print("📋 copy <name>:         Copy the snippet to clipboard")
        print("🗑️  delete <name>:      Delete a snippet")
        print("❓ help:                Display this help menu")
        print("=" * 40)


sc = Snipper()

def main():
    args = sys.argv[1:]

    if len(args) == 0 or args[0].lower() == "help":
        sc.help()
    elif args[0].lower() == "create":
        sc.make_snip(args[1])
    elif args[0].lower() == "list":
        sc.list()
    elif args[0].lower() == "open":
        sc.open(args[1])
    elif args[0].lower() == "copy":
        sc.copy(args[1])
    elif args[0].lower() == "delete":
        sc.delete(args[1])
    else:
        print("⚠️  Invalid command! Use 'help' to see available commands.\n")

if __name__ == '__main__':
    main()
