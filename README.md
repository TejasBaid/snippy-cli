Here’s the updated **`README.md`** file with the **primary installation** method set as **PyPI** and the **manual installation** as a secondary option. I’ve updated the links accordingly:


# 📝 Snippy - A Simple CLI for Managing Code Snippets (v1.0.0)

Snippy is a lightweight command-line interface (CLI) tool for managing code snippets efficiently. With Snippy, you can create, edit, copy, and delete snippets right from your terminal. It's designed to help developers quickly store and retrieve useful code snippets, all while keeping things simple and straightforward.

## 🚀 Features
- 📂 **Create, list, and manage snippets** easily.
- ✏️ **Open snippets** in your preferred text editor.
- 📋 **Copy snippets** directly to the clipboard.
- 🗑️ **Delete snippets** when they are no longer needed.

## 📦 Installation

### From PyPI (Recommended)

The easiest way to install Snippy is from [PyPI](https://pypi.org/project/snippy-cli/). Just run the following command:

```bash
pip install snippy-cli
```

This will install **snippy-cli** and its dependencies, making it available as a command-line tool that you can run directly.

### Manual Installation

If you prefer to install manually, you can clone the repository and install the package locally.

1. **Clone the repository**:
   ```bash
   git clone https://github.com/TejasBaid/snippy-cli.git
   cd snippy-cli
   ```

2. **Install the package**:
   ```bash
   pip install .
   ```

> **Note**: Make sure you have Python 3.x and `pip` installed.

## 🛠️ Usage

Once installed, Snippy can be used directly from the terminal using the `snip` command.

### Example Commands:

- **Create a new snippet**:
   ```bash
   snip create my_snippet
   ```
   This command opens your default text editor to create a snippet. The snippet will be saved in the `Snippets/` directory.

- **List all snippets**:
   ```bash
   snip list
   ```

- **Open a snippet for editing**:
   ```bash
   snip open my_snippet
   ```

- **Copy a snippet to the clipboard**:
   ```bash
   snip copy my_snippet
   ```

- **Delete a snippet**:
   ```bash
   snip delete my_snippet
   ```

- **Display help**:
   ```bash
   snip help
   ```

## 📖 Available Commands

| Command                      | Description                                         |
|-------------------------------|-----------------------------------------------------|
| `snip create <snippet_name>`   | Create a new snippet                                |
| `snip list`                    | List all snippets                                   |
| `snip open <snippet_name>`     | Open an existing snippet for editing                |
| `snip copy <snippet_name>`     | Copy the snippet's content to the clipboard         |
| `snip delete <snippet_name>`   | Delete a snippet                                    |
| `snip help`                    | Display this help message                           |

## 📜 Versioning

This is **snippy-cli v1.0.0**, which includes the following features:

- **Snippet management**: Create, list, open, edit, copy, and delete snippets from the command line.
- **Clipboard functionality**: Easily copy snippet content to your clipboard.
- **Interactive mode** (planned for future versions).

Stay tuned for more updates in future versions!

## 🤝 Contributing

Feel free to submit pull requests, open issues, or suggest new features! Contributions are welcome. To contribute:

1. Fork the repository.
2. Create a new feature branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -m "Add some feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgements

- Thanks to the open-source community for the inspiration and support.
```

### Key Changes:
- **Primary installation**: I set the **PyPI** installation as the recommended method with the provided link: [https://pypi.org/project/snippy-cli/](https://pypi.org/project/snippy-cli/).
- **Manual installation**: I moved the repository clone and local installation to a secondary, optional section.

This structure should now clearly guide users to install from PyPI, while still offering a manual installation method if needed.

Let me know if any other adjustments are needed!