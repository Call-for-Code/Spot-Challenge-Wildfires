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

## What's in each folder

Good question! Let's take a look at the directory structure here. You do not need to understand the details to use this scoring script, but if you are curious, here we go:

- `annotations`: This folder contains the Ground Truth (real observations) for each phase. Initially, only the one for the `dev` phase, called `actual_simplified_dev.csv`, has real data in it and the rest include only two lines. We will publish the new ground truths as each phase closes. 
  - Note: Make sure to pull the updates from this repo to get the new annotations as they become available. The scoring script will return zero for phases where the annotation file has only two lines. So initially, only the `dev` phase will give you a non-zero score. 
- `evaluation_scripts`: This folder contains the evaluation scripts that are used in the backend. You can read through the `main.py` script if you want to know exactly how the format checking and scoring are done
- `local_evaluate.py`: This is the main script that you will use. It is a CLI (command line interface) that simplifies usage of the actual evaluation script.
- `requirements.txt`: This is the file you can use to install the required libraries. see the [Requirements](###Requirements) section for more info. 
- `README.md`: That's the file you are reading now! Hello 👋

Good luck!