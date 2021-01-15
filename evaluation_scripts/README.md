# Local Scoring Script
This script lets you score your submissions locally. You can use this at anytime to score your `csv` submissions on your machine.

## Usage

### Requirements
**Note: You needs Python 3.6 and above to run this script**
You need the latest `pandas` and `numpy` to run this script. To install them you can run the following command inside this folder.

```
pip install -r requirements.txt
```

### Running the script
To use this script run the `local_evaluate.py` script with arguments `--phase`, and `--submission_path`. The phase denotes which phase you want to score, and the submission_path is the path to your csv file. 

This is an example of what your command might look like.

```
python ./local_evaluate.py --phase dev --submission_path ./my_submission.csv
```

### Description of the arguments

| Argument            | Expected Value                                      |
| ------------------- | --------------------------------------------------- |
| `--phase`           | Valid options are `dev`, `week3`, `week4`, or `feb` |
| `--submission_path` | Enter the path to the `csv` file you want to score. |

*Note: You can get help from the script by invoking `python ./local_evaluate.py -h`*