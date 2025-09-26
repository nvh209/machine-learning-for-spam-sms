# Setting Up a Python Virtual Environment

To ensure that all dependencies are handled correctly, it's advisable to run this project in a Python virtual environment. This helps keep dependencies required by different projects separate and organized. Follow these steps to set up your virtual environment:

## Step 1: Create the Virtual Environment

First, you need to create a virtual environment in your project directory. Run the following command in your terminal:

```bash
python -m venv .venv
```

This command creates a new directory named `.venv` in your current directory, containing the virtual environment.

## Step 2: Activate the Virtual Environment

Before you can start installing packages, you need to activate the virtual environment. Activation differs based on your operating system.

- **On macOS and Linux:**

  ```bash
  source .venv/bin/activate
  ```

- **On Windows:**

  ```cmd
  .\.venv\Scripts\activate
  ```

Activating the virtual environment will change your shell’s prompt to show what virtual environment you’re using, and modify the environment so that running `python` will get you that particular version and installation of Python.

## Step 3: Install Required Packages

Once the virtual environment is activated, you can install the required packages by running the following command:

```bash
pip install -r requirements.txt
```

This command reads the `requirements.txt` file in your project directory and installs all the necessary packages as specified in that file.