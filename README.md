# Call Event Analyzer

This project analyzes call events to identify suspicious call behavior based on the duration of the calls. It processes call and hangup events to calculate the average call duration for each caller and identifies suspects whose average call duration is under 5 seconds.

## Requirements

Please ensure the Python version is at least 3.7. You can also check the version with the following.

```bash
python --version
```

Either download or update the Python through [Download Python](https://www.python.org/downloads/)

Also, make sure the data text file is in the same directory as the code file.

## Usage
Assume the folder's directory is on the desktop.
```bash
cd desktop
cd hiya_coding_challenge 
python call_event_analyzer.py
Please enter the name of the data file (e.g. exampleInput.txt): exampleInput.txt
The list of suspicious callers is as follows.
['Bob']
```

## License

[MIT](https://choosealicense.com/licenses/mit/)