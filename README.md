# client_review_converter

The converter takes the output from the "Client Advisory Review" export and creates a list of clients that need a review done before their client anniversary date.

## Description



## Getting Started

### Dependencies

It runs on Python 3.9.7 and uses csv, tkinter, and Path.  csv and tkinter are to allow a user to choose a file from their computer.  Path helps work with file paths.

### Installing

Simply run the python code from the command line or it can be converted into an executable with pyinstaller

### Executing program

The input file should be the standard format from the LPL export function, specifically the last review date in column 1, Name in column 2, and Client since in Column 11.  No additional formating is required if it is downloaded in the standard .csv format.

run the script from the command line and when prompted choose the input file.

The output file will be created "clients_needing_reviews.csv" in the same directory as the python folder.

## Help



## Authors

Contributors names and contact info

Michael Canavan

## Version History


* 0.1
    * Initial Release

## License

This project is open source under the MIT License

## Acknowledgments
