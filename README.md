# Developer Environment Setup Wiki
## Visual Studio Code & PyCharm Installation Guide

## Table of Contents
- [Visual Studio Code](#visual-studio-code)
  - [Downloading and Installing VS Code](#downloading-and-installing-vs-code)
  - [Essential VS Code Extensions for Python](#essential-vs-code-extensions-for-python)
  - [Common VS Code Commands and Shortcuts](#common-vs-code-commands-and-shortcuts)
- [PyCharm](#pycharm)
  - [Downloading and Installing PyCharm](#downloading-and-installing-pycharm)
  - [Setting Up Python Interpreter in PyCharm](#setting-up-python-interpreter-in-pycharm)
  - [Common PyCharm Commands and Shortcuts](#common-pycharm-commands-and-shortcuts)
- [Python Environment Setup](#python-environment-setup)
  - [Creating Virtual Environments](#creating-virtual-environments)
  - [Managing Packages](#managing-packages)

---

## Visual Studio Code

### Downloading and Installing VS Code

1. **Go to the official website**: [https://code.visualstudio.com](https://code.visualstudio.com)
2. **Download the appropriate version** for your operating system:
   - **Windows**: Click the download button for Windows
   - **macOS**: Click the download button for Mac
   - **Linux**: Choose the appropriate package for your distribution

3. **Install VS Code**:
   - **Windows**: Run the downloaded installer and follow the prompts
   - **macOS**: Drag Visual Studio Code.app to the Applications folder
   - **Linux**: Use the package manager for your distribution or follow the instructions on the download page

4. **Launch VS Code** after installation completes

### Essential VS Code Extensions for Python

Open VS Code and install these extensions by clicking the Extensions icon in the sidebar (or press `Ctrl+Shift+X`) and searching for:

1. **Python** (by Microsoft) - Essential Python language support
2. **Pylance** - Fast, feature-rich language support for Python
3. **Jupyter** - For working with Jupyter notebooks
4. **Python Indent** - Correct indentation for Python code
5. **autoDocstring** - Generates documentation strings for Python functions
6. **Python Test Explorer** - Run and debug tests

### Common VS Code Commands and Shortcuts

#### General Commands

| Action | Windows/Linux | macOS |
|--------|--------------|-------|
| Open Command Palette | `Ctrl+Shift+P` | `Cmd+Shift+P` |
| Quick Open File | `Ctrl+P` | `Cmd+P` |
| Open Settings | `Ctrl+,` | `Cmd+,` |
| Toggle Terminal | ``Ctrl+` `` | ``Cmd+` `` |
| Toggle Sidebar | `Ctrl+B` | `Cmd+B` |
| Open New Window | `Ctrl+Shift+N` | `Cmd+Shift+N` |
| Save File | `Ctrl+S` | `Cmd+S` |

#### Python-specific Commands

| Action | Windows/Linux | macOS |
|--------|--------------|-------|
| Run Python File | `F5` or right-click → Run Python File in Terminal | `F5` or right-click → Run Python File in Terminal |
| Start/Continue Debugging | `F5` | `F5` |
| Run Selection/Line | `Shift+Enter` | `Shift+Enter` |
| Select Python Interpreter | `Ctrl+Shift+P` → "Python: Select Interpreter" | `Cmd+Shift+P` → "Python: Select Interpreter" |
| Format Document | `Shift+Alt+F` | `Shift+Option+F` |
| Run Python Tests | `Ctrl+Shift+P` → "Python: Run All Tests" | `Cmd+Shift+P` → "Python: Run All Tests" |

#### Additional Terminal Commands

Open the integrated terminal in VS Code (``Ctrl+` `` or ``Cmd+` ``) and use these commands:

```bash
# Create a virtual environment
python -m venv venv

# Activate virtual environment
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# Install packages
pip install package-name

# Run a Python script
python script.py
```

---

## PyCharm

### Downloading and Installing PyCharm

1. **Go to the official website**: [https://www.jetbrains.com/pycharm/download](https://www.jetbrains.com/pycharm/download)
2. **Choose your edition**:
   - **Community Edition**: Free, open-source version
   - **Professional Edition**: Paid version with additional features (free trial available)

3. **Download the appropriate version** for your operating system
4. **Install PyCharm**:
   - **Windows**: Run the downloaded installer and follow the prompts
   - **macOS**: Mount the disk image and drag PyCharm to the Applications folder
   - **Linux**: Extract the tarball and run the pycharm.sh script in the bin directory

5. **First-time setup**:
   - When you first launch PyCharm, you may be asked to import settings
   - Choose whether to send usage statistics
   - Select your UI theme (Darcula or Light)

### Setting Up Python Interpreter in PyCharm

1. **Open PyCharm** and create a new project or open an existing one
2. **Configure Python Interpreter**:
   - Go to **File → Settings** (Windows/Linux) or **PyCharm → Preferences** (macOS)
   - Navigate to **Project: [YourProjectName] → Python Interpreter**
   - Click the gear icon → **Add**
   - Choose the type of interpreter:
     - **System Interpreter**: Use the system-wide Python
     - **Virtual Environment**: Create a new virtual environment or use an existing one
   - Select the Python executable or virtual environment path
   - Click **OK** to apply changes

### Common PyCharm Commands and Shortcuts

#### General Commands

| Action | Windows/Linux | macOS |
|--------|--------------|-------|
| Quick Open (Search Everywhere) | `Shift+Shift` | `Shift+Shift` |
| Open Settings | `Ctrl+Alt+S` | `Cmd+,` |
| Open Terminal | `Alt+F12` | `Option+F12` |
| Find Action | `Ctrl+Shift+A` | `Cmd+Shift+A` |
| Save All | `Ctrl+S` | `Cmd+S` |
| Open Project Structure | `Ctrl+Alt+Shift+S` | `Cmd+;` |
| Recent Files | `Ctrl+E` | `Cmd+E` |

#### Code Editing Commands

| Action | Windows/Linux | macOS |
|--------|--------------|-------|
| Code Completion | `Ctrl+Space` | `Ctrl+Space` |
| Quick Documentation | `Ctrl+Q` | `Ctrl+J` |
| Go to Declaration | `Ctrl+B` | `Cmd+B` |
| Find Usages | `Alt+F7` | `Option+F7` |
| Rename | `Shift+F6` | `Shift+F6` |
| Format Code | `Ctrl+Alt+L` | `Cmd+Option+L` |
| Comment/Uncomment Line | `Ctrl+/` | `Cmd+/` |
| Duplicate Line | `Ctrl+D` | `Cmd+D` |

#### Running and Debugging

| Action | Windows/Linux | macOS |
|--------|--------------|-------|
| Run Current Configuration | `Shift+F10` | `Ctrl+R` |
| Debug Current Configuration | `Shift+F9` | `Ctrl+D` |
| Run Context Configuration | `Ctrl+Shift+F10` | `Ctrl+Shift+R` |
| Stop Program | `Ctrl+F2` | `Cmd+F2` |
| Toggle Breakpoint | `Ctrl+F8` | `Cmd+F8` |
| Step Over | `F8` | `F8` |
| Step Into | `F7` | `F7` |
| Step Out | `Shift+F8` | `Shift+F8` |
| Resume Program | `F9` | `F9` |

#### Version Control

| Action | Windows/Linux | macOS |
|--------|--------------|-------|
| VCS Operations Popup | `Alt+` | `Ctrl+V` |
| Commit Changes | `Ctrl+K` | `Cmd+K` |
| Update Project | `Ctrl+T` | `Cmd+T` |
| Show Diff | `Ctrl+D` | `Cmd+D` |
| Show History | `Ctrl+Shift+H` | `Cmd+Shift+H` |

---

## Python Environment Setup

### Creating Virtual Environments

Virtual environments isolate dependencies for different projects.

#### Using venv (built-in)

```bash
# Create a virtual environment
python -m venv venv

# Activate virtual environment
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# Deactivate virtual environment
deactivate
```

#### Using conda (if Anaconda/Miniconda is installed)

```bash
# Create a conda environment
conda create --name myenv python=3.9

# Activate conda environment
conda activate myenv

# Deactivate conda environment
conda deactivate
```

### Managing Packages

#### Using pip

```bash
# Install a package
pip install package-name

# Install specific version
pip install package-name==1.2.3

# Install from requirements file
pip install -r requirements.txt

# List installed packages
pip list

# Generate requirements file
pip freeze > requirements.txt

# Upgrade a package
pip install --upgrade package-name

# Uninstall a package
pip uninstall package-name
```

#### Using conda (if Anaconda/Miniconda is installed)

```bash
# Install a package
conda install package-name

# Install from a specific channel
conda install -c conda-forge package-name

# List installed packages
conda list

# Update all packages
conda update --all

# Update specific package
conda update package-name

# Remove a package
conda remove package-name
```
