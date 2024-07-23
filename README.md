# SmartVenv

SmartVenv is a smarter virtual environment and dependency management tool for Python, designed to simplify and enhance your development workflow. With a single command, you can create virtual environments, install dependencies, and ensure compatibility, all while keeping your projects isolated and clean.

## Features

- **Single Command Installation**: Automatically create and activate virtual environments, and install packages or dependencies from `requirements.txt` with just one command.
- **Dependency Resolution**: Smartly resolve and install packages with correct versions to avoid conflicts and ensure compatibility.
- **Lock Dependencies**: Generate a lock file to freeze exact versions of installed packages for reproducible environments.
- **Easy Management**: List, update, and remove packages effortlessly.
- **Cross-Platform**: Works seamlessly on both Unix-like systems and Windows.

## Installation

### From PyPI

```sh
pip install smartvenv
```

### From Homebrew

```sh
brew tap roshanlam/smartvenv
brew install smartvenv
```

## Usage

### Create and Install Dependencies

To create a virtual environment and install dependencies from a `requirements.txt` file:

```sh
smartvenv -r requirements.txt
```

### Install Specific Packages

To install specific packages with dependency resolution:

```sh
smartvenv install requests flask
```

### Install Both `requirements.txt` and Specific Packages

To install dependencies from `requirements.txt` and additional packages:

```sh
smartvenv -r requirements.txt install requests flask
```

### List Installed Packages

To list all installed packages in the virtual environment:

```sh
smartvenv list
```

### Update All Packages

To update all installed packages to their latest versions:

```sh
smartvenv update
```

### Remove a Specific Package

To remove a specific package:

```sh
smartvenv remove --package requests
```

### Clean (Delete) the Virtual Environment

To clean up (delete) the virtual environment:

```sh
smartvenv clean
```

## Example Workflow

Here's an example of a typical workflow using SmartVenv:

1. **Create and install dependencies from `requirements.txt`**:
   ```sh
   smartvenv -r requirements.txt
   ```

2. **Install additional packages**:
   ```sh
   smartvenv install django numpy
   ```

3. **Generate a lock file**:
   ```sh
   smartvenv lock
   ```

4. **List installed packages**:
   ```sh
   smartvenv list
   ```

5. **Update all packages**:
   ```sh
   smartvenv update
   ```

6. **Remove a specific package**:
   ```sh
   smartvenv remove --package flask
   ```

7. **Clean up the virtual environment**:
   ```sh
   smartvenv clean
   ```
