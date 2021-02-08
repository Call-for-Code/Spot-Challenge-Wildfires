import argparse
import inspect
import json
import os
import sys

import evaluation_script


# 
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
#


## CONSTANTS ########################################
SUBMISSION_METADATA = {
    "status": u"running",
    "when_made_public": None,
    "participant_team": 5,
    "input_file": "https://abc.xyz/path/to/submission/file.json",
    "execution_time": u"123",
    "publication_url": u"ABC",
    "challenge_phase": 1,
    "created_by": u"ABC",
    "stdout_file": "https://abc.xyz/path/to/stdout/file.json",
    "method_name": u"Test",
    "stderr_file": "https://abc.xyz/path/to/stderr/file.json",
    "participant_team_name": u"Test Team",
    "project_url": u"http://foo.bar",
    "method_description": u"ABC",
    "is_public": False,
    "submission_result_file": "https://abc.xyz/path/result/file.json",
    "id": 123,
    "submitted_at": u"2017-03-20T19:22:03.880652Z",
}

ANNOTATION_PATHS={
    'dev'  : 'annotations/actual_simplified_dev.csv',
    'week3': 'annotations/actual_simplified_week_3.csv',
    'week4': 'annotations/actual_simplified_week_4.csv',
    'feb'  : 'annotations/actual_simplified_feb.csv',
}

## PARSING THE ARGUMENTS ########################################
parser = argparse.ArgumentParser(description='Score your submissions locally. Note that for phases that are not available yet, the script will return the score of 0')

parser.add_argument('--phase', required=True, help='Select which phase you want to score', choices=['dev', 'week3', 'week4', 'feb'])
parser.add_argument('--submission_path', required=True, help="This is the path to your submissions csv file. Follow the guidelines from the challenge page.")

args = parser.parse_args()

## SCORING THE SUBMISSION ########################################
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

if args.submission_path[:4] == "http":
    qualified_submission_path = args.submission_path
else:
    qualified_submission_path = os.path.join(currentdir, args.submission_path)

result = evaluation_script.evaluate(
    os.path.join(currentdir, ANNOTATION_PATHS[args.phase]),
    qualified_submission_path,
    args.phase,
    submission_metadata=SUBMISSION_METADATA
)
print("All informative error metrics: \n{}".format(json.dumps(result['submission_result'],sort_keys=True, indent=4)))
print("Scoring errors: \n\tMAE: {:.4f} \n\tRMSE: {:.4f} \n\tTotal: {:.4f}".format(
        result['submission_result']['mae'],
        result['submission_result']['rmse'],
        result['submission_result']['tot']
    ))

if result['submission_result']['mae'] == -99: 
    print ("Note: -99 means that the ground truth is not available")
