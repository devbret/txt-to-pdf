# TXT-To-PDF

A Python utility which converts all `.txt` files in an input directory into corresponding `.pdf` files in an output directory using the `ReportLab` library.

## Overview

The script reads each text file line by line and renders the content onto a letter-sized PDF canvas with consistent margins and spacing. As text is written to the page, the script automatically creates new pages when the vertical space runs out, ensuring the entire document is preserved in the resulting PDF.

The program also includes structured `logging` using Python’s built-in logging module. It records each stage of the process while capturing any errors which occur. All events are logged both to the console and to a `conversion.log` file, allowing users to monitor progress and troubleshoot issues during the conversion process.
