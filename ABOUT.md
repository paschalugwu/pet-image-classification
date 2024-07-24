# Notes: Frequently Asked Questions for Image Classification Project

These notes address frequently asked questions (FAQ) regarding the image classification project in this repository. These FAQs have been compiled to help clarify common points of confusion about the project.

&nbsp;

## Quick Links to Frequently Asked Questions
* [GitHub Repository Link](https://github.com/<your-username>/<your-repo-name>)
* [Issues with the Project Workspace](https://github.com/<your-username>/<your-repo-name>/blob/main/notes/project_intro-to-python.md#issues-with-the-project-workspace)
* [Running the Project on a Local Computer](https://github.com/<your-username>/<your-repo-name>/blob/main/notes/project_intro-to-python.md#running-the-project-on-a-local-computer)
* [Files Required to Run `check_images.py` Locally](https://github.com/<your-username>/<your-repo-name>/blob/main/notes/project_intro-to-python.md#files-required-to-run-check_imagespy-locally)
* [Running Batch Files on Windows OS Locally](https://github.com/<your-username>/<your-repo-name>/blob/main/notes/project_intro-to-python.md#running-batch-files-on-windows-os-locally)
* [Hints for this Project](https://github.com/<your-username>/<your-repo-name>/blob/main/notes/project_intro-to-python.md#hints-for-this-project)
* [Eliminating Syntax Errors with Text Editor/IDE](https://github.com/<your-username>/<your-repo-name>/blob/main/notes/project_intro-to-python.md#eliminating-syntax-errors-with-text-editorintegrated-development-environment)
* [Cutting and Pasting Code in the Classroom](https://github.com/<your-username>/<your-repo-name>/blob/main/notes/project_intro-to-python.md#cutting-and-pasting-code-in-the-classroom)
* [Indentation of Python Code](https://github.com/<your-username>/<your-repo-name>/blob/main/notes/project_intro-to-python.md#indention-of-python-code)
* [Replacing None and Pass Statements](https://github.com/<your-username>/<your-repo-name>/blob/main/notes/project_intro-to-python.md#replacing-none-and-pass-statements)

&nbsp;

## Issues with the Project Workspace
If you encounter issues with the Project Workspace, such as files not loading or slow performance, try the following:
* Restart your web browser.
* Switch to a different browser, such as Chrome or Firefox.

If these steps do not resolve the issue, you can complete the project on a local computer using the instructions provided in the [FAQ](https://github.com/<your-username>/<your-repo-name>/blob/main/notes/project_intro-to-python.md#running-the-project-on-a-local-computer).

&nbsp;

## Running the Project on a Local Computer
For local execution, ensure you have Python 3.6 installed. You can use [Anaconda](https://www.anaconda.com/download) to manage Python and packages. Follow the instructions from **2. Intro to Python**, **Lesson 5. Scripting**, **Section 3** to install Anaconda.

### Installing PyTorch and torchvision
Install the required Python packages using the instructions available on [PyTorch's Get Started page](http://pytorch.org/).

&nbsp;

## Files Required to Run `check_images.py` Locally
Ensure the following files and folders are in the same directory as `check_images.py`:
* `pet_images` (folder with pet images)
* `uploaded_images` (folder for uploaded images)
* `classifier.py`
* `dognames.txt`
* `imagenet1000_clsid_to_human.txt`
* `adjust_results4_isadog.py`
* `calculates_results_stats.py`
* `classify_images.py`
* `get_input_args.py`
* `get_pet_labels.py`
* `print_results.py`
* `run_models_batch.sh`
* `run_models_batch.bat`
* `run_models_batch_uploaded.sh`
* `run_models_batch_uploaded.bat`
* `test_classifier.py`
* `print_functions_for_lab_checks.py`

Hints files end with `_hints.py` and are available in the repository and Project Workspace:
* `adjust_results4_isadog_hints.py`
* `calculates_results_stats_hints.py`
* `classify_images_hints.py`
* `get_input_args_hints.py`
* `get_pet_labels_hints.py`
* `print_results_hints.py`

&nbsp;

## Running Batch Files on Windows OS Locally
To run batch files on Windows, use files ending with `.bat` instead of `.sh`. Ensure Anaconda is installed. Use the Anaconda Prompt to navigate to the folder with the project files and execute:
```terminal
run_models_batch.bat
```
For uploaded images, use `run_models_batch_uploaded.bat` instead.

&nbsp;

## Hints for this Project
Instructor-provided hints files help guide you through the project. They are located in the Project Workspace and repository:
* `adjust_results4_isadog_hints.py`
* `calculates_results_stats_hints.py`
* `classify_images_hints.py`
* `get_input_args_hints.py`
* `get_pet_labels_hints.py`
* `print_results_hints.py`

&nbsp;

## Eliminating Syntax Errors with Text Editor/IDE
If syntax errors occur, consider using a text editor or IDE like Atom, Sublime Text, or Notepad++ to check your code. The Spyder IDE is available through Anaconda Navigator.

&nbsp;

## Cutting and Pasting Code in the Classroom
Avoid cutting and pasting code directly from the classroom to prevent syntax errors due to font differences and indentation issues.

&nbsp;

## Indentation of Python Code
Python uses indentation to define code blocks. Follow the [PEP8 Style Guide](https://www.python.org/dev/peps/pep-0008/) which recommends using 4 spaces for each indentation level.

&nbsp;

## Replacing None and Pass Statements
Replace `None` or `pass` statements in your code with the appropriate function implementations. `pass` is a placeholder, and `None` represents the absence of a value.
