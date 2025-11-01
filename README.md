# Txt-To-PDF

Txt-To-PDF converts all `.txt` files within an input directory into corresponding `.pdf` files in an output directory using the ReportLab library. It ensures the output folder exists, reads each text file line by line and writes the text onto a letter-sized PDF canvas with consistent margins and line spacing.

When vertical space runs out on a page, this Python script automatically adds a new one and continues writing. Each conversion is logged to the console and once all files are processed, it prints a final confirmation message indicating completion.

The script also uses Python’s built-in `logging` module to record each stage of the conversion process, including directory creation, file reading and PDF generation. All actions and errors are logged both to the console and a `conversion.log` file.
