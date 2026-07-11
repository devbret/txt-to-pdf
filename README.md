# TXT-To-PDF

Python utility which converts all `.txt` files in an input directory into corresponding `.pdf` files in an output directory using the `ReportLab` library.

## Application Overview

The script reads each text file line by line and renders the content onto a letter-sized PDF canvas with consistent margins and spacing. As text is written to the page, the script automatically creates new pages when the vertical space runs out, ensuring the entire document is preserved in the resulting PDF.

The program also includes structured `logging` using Python’s built-in logging module. It records each stage of the process while capturing any errors which occur. All events are logged both to the console and to a `conversion.log` file, allowing users to monitor progress and troubleshoot issues during the conversion process.

## Basic Setup Instructions

Below are instructions for installing and running this application on a Linux machine.

### Programs Needed

- [Git](https://git-scm.com/downloads)

- [Python](https://www.python.org/downloads/)

### Steps

1. Install the above programs

2. Open a terminal

3. Clone this repository: `git clone git@github.com:devbret/txt-to-pdf.git`

4. Navigate to the repo's directory: `cd txt-to-pdf`

5. Create a virtual environment: `python3 -m venv venv`

6. Activate your virtual environment: `source venv/bin/activate`

7. Install the needed dependencies: `pip install -r requirements.txt`

8. Place your `.txt` files into the `input` directory of this repo

9. Run the application: `python3 app.py`

10. The results will be returned to you in the `output` directory of this repo as `.pdf` files

11. Exit the virtual environment: `deactivate`

## Other Considerations

This project repo is intended to demonstrate an ability to do the following:

- Convert every `.txt` file in the `input` directory into a PDF in the `output` directory using `ReportLab`

- Wrap lines to fit inside page margins and preserve leading indentation as a hanging indent

- Log each stage of the conversion to both the console and a `conversion.log` file

- Finish with a summary of how many files were converted or failed during the process

If you have any questions or would like to collaborate, please reach out either on GitHub or via [my website](https://bretbernhoft.com/).
