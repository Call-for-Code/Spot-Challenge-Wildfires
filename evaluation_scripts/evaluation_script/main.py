import os.path
import json
import pkg_resources

# Check required libraries are present
try:
    pkg_resources.require("pandas>=1.2.0")
    pkg_resources.require("numpy>=1.19.0")
except pkg_resources.DistributionNotFound:
    print("Installing numpy pandas")
    os.system("pip install numpy pandas")
except pkg_resources.VersionConflict:
    print("Updating numpy pandas")
    os.system("pip install --upgrade pandas")
except:
    print("An exception occurred numpy pandas")

import numpy as np
import pandas as pd

EPSILON = 1e-10

SKIP_TEST_PHASE = False
CONFIG = {
    "dev": {
        "name": "Development Phase",
        "split": "feb2020_actual",
        "skip": False,
    },
    "week3": {
        "name": "Predict January Week 3",
        "split": "jan2021_week3_actual",
        "skip": False,
    },
    "week4": {
        "name": "Predict January Week 4",
        "split": "jan2021_week4_actual",
        "skip": False,
    },
    "feb": {
        "name": "[Final] Predict February",
        "split": "feb2021_actual",
        "skip": False,
    }
}

VALID_COLUMNS = ["Date", "Region", "Estimated_fire_area"]
VALID_REGION_CODES = ["NSW", "NT", "QL", "SA", "TA", "VI", "WA"]
VALID_DATE_RANGE_FEB_2020 =       pd.date_range(start='02/01/2020', end='02/28/2020')
VALID_DATE_RANGE_FEB_2021 =       pd.date_range(start='02/01/2021', end='02/28/2021')
VALID_DATE_RANGE_JAN_WEEK3_2021 = pd.date_range(start='01/16/2021', end='01/22/2021')
VALID_DATE_RANGE_JAN_WEEK4_2021 = pd.date_range(start='01/23/2021', end='01/29/2021')

pd.set_option("display.max_rows", None, "display.max_columns", None)


class formatException(Exception):
    pass

class missingValueException(Exception):
    pass

class cleaningException(Exception):
    pass


def _error(actual: np.ndarray, predicted: np.ndarray):
    """ Simple error """
    return actual - predicted


def _percentage_error(actual: np.ndarray, predicted: np.ndarray):
    """
    Percentage error
    Note: result is NOT multiplied by 100
    """
    return _error(actual, predicted) / (actual + EPSILON)


def _naive_forecasting(actual: np.ndarray, seasonality: int = 1):
    """ Naive forecasting method which just repeats previous samples """
    return actual[:-seasonality]


def _relative_error(actual: np.ndarray, predicted: np.ndarray, benchmark: np.ndarray = None):
    """ Relative Error """
    if benchmark is None or isinstance(benchmark, int):
        # If no benchmark prediction provided - use naive forecasting
        if not isinstance(benchmark, int):
            seasonality = 1
        else:
            seasonality = benchmark
        return _error(actual[seasonality:], predicted[seasonality:]) /\
               (_error(actual[seasonality:], _naive_forecasting(actual, seasonality)) + EPSILON)

    return _error(actual, predicted) / (_error(actual, benchmark) + EPSILON)


def _bounded_relative_error(actual: np.ndarray, predicted: np.ndarray, benchmark: np.ndarray = None):
    """ Bounded Relative Error """
    if benchmark is None or isinstance(benchmark, int):
        # If no benchmark prediction provided - use naive forecasting
        if not isinstance(benchmark, int):
            seasonality = 1
        else:
            seasonality = benchmark

        abs_err = np.abs(_error(actual[seasonality:], predicted[seasonality:]))
        abs_err_bench = np.abs(_error(actual[seasonality:], _naive_forecasting(actual, seasonality)))
    else:
        abs_err = np.abs(_error(actual, predicted))
        abs_err_bench = np.abs(_error(actual, benchmark))

    return abs_err / (abs_err + abs_err_bench + EPSILON)


def _geometric_mean(a, axis=0, dtype=None):
    """ Geometric mean """
    if not isinstance(a, np.ndarray):  # if not an ndarray object attempt to convert it
        log_a = np.log(np.array(a, dtype=dtype))
    elif dtype:  # Must change the default dtype allowing array type
        if isinstance(a, np.ma.MaskedArray):
            log_a = np.log(np.ma.asarray(a, dtype=dtype))
        else:
            log_a = np.log(np.asarray(a, dtype=dtype))
    else:
        log_a = np.log(a)
    return np.exp(log_a.mean(axis=axis))


def mse(actual: np.ndarray, predicted: np.ndarray):
    """ Mean Squared Error """
    return np.mean(np.square(_error(actual, predicted)))


def rmse(actual: np.ndarray, predicted: np.ndarray):
    """ Root Mean Squared Error """
    return np.sqrt(mse(actual, predicted))


def nrmse(actual: np.ndarray, predicted: np.ndarray):
    """ Normalized Root Mean Squared Error """
    return rmse(actual, predicted) / (actual.max() - actual.min())


def me(actual: np.ndarray, predicted: np.ndarray):
    """ Mean Error """
    return np.mean(_error(actual, predicted))


def mae(actual: np.ndarray, predicted: np.ndarray):
    """ Mean Absolute Error """
    return np.mean(np.abs(_error(actual, predicted)))


mad = mae  # Mean Absolute Deviation (it is the same as MAE)


def gmae(actual: np.ndarray, predicted: np.ndarray):
    """ Geometric Mean Absolute Error """
    return _geometric_mean(np.abs(_error(actual, predicted)))


def mdae(actual: np.ndarray, predicted: np.ndarray):
    """ Median Absolute Error """
    return np.median(np.abs(_error(actual, predicted)))


def mpe(actual: np.ndarray, predicted: np.ndarray):
    """ Mean Percentage Error """
    return np.mean(_percentage_error(actual, predicted))


def mape(actual: np.ndarray, predicted: np.ndarray):
    """
    Mean Absolute Percentage Error
    Properties:
        + Easy to interpret
        + Scale independent
        - Biased, not symmetric
        - Undefined when actual[t] == 0
    Note: result is NOT multiplied by 100
    """
    return np.mean(np.abs(_percentage_error(actual, predicted)))


def mdape(actual: np.ndarray, predicted: np.ndarray):
    """
    Median Absolute Percentage Error
    Note: result is NOT multiplied by 100
    """
    return np.median(np.abs(_percentage_error(actual, predicted)))


def smape(actual: np.ndarray, predicted: np.ndarray):
    """
    Symmetric Mean Absolute Percentage Error
    Note: result is NOT multiplied by 100
    """
    return np.mean(2.0 * np.abs(actual - predicted) / ((np.abs(actual) + np.abs(predicted)) + EPSILON))


def smdape(actual: np.ndarray, predicted: np.ndarray):
    """
    Symmetric Median Absolute Percentage Error
    Note: result is NOT multiplied by 100
    """
    return np.median(2.0 * np.abs(actual - predicted) / ((np.abs(actual) + np.abs(predicted)) + EPSILON))


def maape(actual: np.ndarray, predicted: np.ndarray):
    """
    Mean Arctangent Absolute Percentage Error
    Note: result is NOT multiplied by 100
    """
    return np.mean(np.arctan(np.abs((actual - predicted) / (actual + EPSILON))))


def mase(actual: np.ndarray, predicted: np.ndarray, seasonality: int = 1):
    """
    Mean Absolute Scaled Error
    Baseline (benchmark) is computed with naive forecasting (shifted by @seasonality)
    """
    return mae(actual, predicted) / mae(actual[seasonality:], _naive_forecasting(actual, seasonality))


def std_ae(actual: np.ndarray, predicted: np.ndarray):
    """ Normalized Absolute Error """
    __mae = mae(actual, predicted)
    return np.sqrt(np.sum(np.square(_error(actual, predicted) - __mae))/(len(actual) - 1))


def std_ape(actual: np.ndarray, predicted: np.ndarray):
    """ Normalized Absolute Percentage Error """
    __mape = mape(actual, predicted)
    return np.sqrt(np.sum(np.square(_percentage_error(actual, predicted) - __mape))/(len(actual) - 1))


def rmspe(actual: np.ndarray, predicted: np.ndarray):
    """
    Root Mean Squared Percentage Error
    Note: result is NOT multiplied by 100
    """
    return np.sqrt(np.mean(np.square(_percentage_error(actual, predicted))))


def rmdspe(actual: np.ndarray, predicted: np.ndarray):
    """
    Root Median Squared Percentage Error
    Note: result is NOT multiplied by 100
    """
    return np.sqrt(np.median(np.square(_percentage_error(actual, predicted))))


def rmsse(actual: np.ndarray, predicted: np.ndarray, seasonality: int = 1):
    """ Root Mean Squared Scaled Error """
    q = np.abs(_error(actual, predicted)) / mae(actual[seasonality:], _naive_forecasting(actual, seasonality))
    return np.sqrt(np.mean(np.square(q)))


def inrse(actual: np.ndarray, predicted: np.ndarray):
    """ Integral Normalized Root Squared Error """
    return np.sqrt(np.sum(np.square(_error(actual, predicted))) / np.sum(np.square(actual - np.mean(actual))))


def rrse(actual: np.ndarray, predicted: np.ndarray):
    """ Root Relative Squared Error """
    return np.sqrt(np.sum(np.square(actual - predicted)) / np.sum(np.square(actual - np.mean(actual))))


def mre(actual: np.ndarray, predicted: np.ndarray, benchmark: np.ndarray = None):
    """ Mean Relative Error """
    return np.mean(_relative_error(actual, predicted, benchmark))


def rae(actual: np.ndarray, predicted: np.ndarray):
    """ Relative Absolute Error (aka Approximation Error) """
    return np.sum(np.abs(actual - predicted)) / (np.sum(np.abs(actual - np.mean(actual))) + EPSILON)


def mrae(actual: np.ndarray, predicted: np.ndarray, benchmark: np.ndarray = None):
    """ Mean Relative Absolute Error """
    return np.mean(np.abs(_relative_error(actual, predicted, benchmark)))


def mdrae(actual: np.ndarray, predicted: np.ndarray, benchmark: np.ndarray = None):
    """ Median Relative Absolute Error """
    return np.median(np.abs(_relative_error(actual, predicted, benchmark)))


def gmrae(actual: np.ndarray, predicted: np.ndarray, benchmark: np.ndarray = None):
    """ Geometric Mean Relative Absolute Error """
    return _geometric_mean(np.abs(_relative_error(actual, predicted, benchmark)))


def mbrae(actual: np.ndarray, predicted: np.ndarray, benchmark: np.ndarray = None):
    """ Mean Bounded Relative Absolute Error """
    return np.mean(_bounded_relative_error(actual, predicted, benchmark))


def umbrae(actual: np.ndarray, predicted: np.ndarray, benchmark: np.ndarray = None):
    """ Unscaled Mean Bounded Relative Absolute Error """
    __mbrae = mbrae(actual, predicted, benchmark)
    return __mbrae / (1 - __mbrae)


def mda(actual: np.ndarray, predicted: np.ndarray):
    """ Mean Directional Accuracy """
    return np.mean((np.sign(actual[1:] - actual[:-1]) == np.sign(predicted[1:] - predicted[:-1])).astype(int))

def tot(actual: np.ndarray, predicted: np.ndarray):
    """ Total score """
    return (0.8*mae(actual, predicted)+0.2*rmse(actual, predicted))

METRICS = {
    'mse': mse,
    'rmse': rmse,
    'nrmse': nrmse,
    'me': me,
    'mae': mae,
    'mad': mad,
    'gmae': gmae,
    'mdae': mdae,
    'mpe': mpe,
    'mape': mape,
    'mdape': mdape,
    'smape': smape,
    'smdape': smdape,
    'maape': maape,
    'mase': mase,
    'std_ae': std_ae,
    'std_ape': std_ape,
    'rmspe': rmspe,
    'rmdspe': rmdspe,
    'rmsse': rmsse,
    'inrse': inrse,
    'rrse': rrse,
    'mre': mre,
    'rae': rae,
    'mrae': mrae,
    'mdrae': mdrae,
    'gmrae': gmrae,
    'mbrae': mbrae,
    'umbrae': umbrae,
    'mda': mda,
    'tot': tot
}


def _evaluate(actual: np.ndarray, predicted: np.ndarray, metrics=('mae', 'mse', 'smape', 'umbrae', 'rmse')):
    results = {}
    for name in metrics:
        try:
            results[name] = METRICS[name](actual, predicted)
        except Exception as err:
            results[name] = np.nan
            print('Unable to compute metric {0}: {1}'.format(name, err))
    return results


def evaluate_all(actual: np.ndarray, predicted: np.ndarray):
    return _evaluate(actual, predicted, metrics=set(METRICS.keys()))


def check_sub_columns(forcast_df, phase_codename):
    # Has 3 columns
    if len(forcast_df.columns) != len(VALID_COLUMNS):
        raise formatException("Expected {} columns in the submission. Found {}: {}".format(
            len(VALID_COLUMNS), len(forcast_df.columns), list(forcast_df.columns)))

    # Has correct columns
    missing_columns = set(VALID_COLUMNS) - set(forcast_df.columns)
    if len(missing_columns) > 0:
        raise formatException("Your submission is missing the following columns: {}".format(missing_columns))

    return None

def check_sub_region_code(forcast_df, phase_codename):
    forcast_regions = forcast_df.Region.unique()

    if set(VALID_REGION_CODES) != set(forcast_regions):
        raise formatException("Your submission doesn't contain all region codes. Expected {}. Found {}".format(
            VALID_REGION_CODES, forcast_regions
        ))

def check_sub_dateformat(forcast_df, phase_codename):
    # Check the date formatting
    if pd.to_datetime(forcast_df['Date'], format='%d-%b', errors='coerce').notnull().all():
        pass # Good Format Date
    elif pd.to_datetime(forcast_df['Date'], format='%b-%d', errors='coerce').notnull().all():
        pass # Not Good, but Acceptable Format Date
    else:
        raise formatException("Your Date column cannot be parsed. Please make sure it is in the format described in the submission guidelines")

    return None

def check_sub_has_all_forcasts(forcast_df, phase_codename):
    if phase_codename == 'dev':
        correct_index = pd.MultiIndex.from_product([VALID_DATE_RANGE_FEB_2020,VALID_REGION_CODES], names=('Date', 'Region'))
    elif phase_codename == 'week3':
        correct_index = pd.MultiIndex.from_product([VALID_DATE_RANGE_JAN_WEEK3_2021,VALID_REGION_CODES], names=('Date', 'Region'))
    elif phase_codename == 'week4':
        correct_index = pd.MultiIndex.from_product([VALID_DATE_RANGE_JAN_WEEK4_2021,VALID_REGION_CODES], names=('Date', 'Region'))
    elif phase_codename == 'feb':
        correct_index = pd.MultiIndex.from_product([VALID_DATE_RANGE_FEB_2021,VALID_REGION_CODES], names=('Date', 'Region'))
    else:
        raise cleaningException("An error happened while parsing phase_codename {}".format(phase_codename))
    
    if len(forcast_df.index) != len(correct_index):
        raise formatException("Your forcast has {} rows, while we expected {} rows.".format(len(forcast_df.index), len(correct_index)))

    if len(correct_index.difference(forcast_df.index)) != 0:
        raise missingValueException("Your submission is missing the following expected forcasts: \n{}. \n Found: \n {}". format(correct_index.difference(forcast_df.index).to_frame(index=False), forcast_df.index.to_frame(index=False)))

    return None

def check_both_indices_match(forcast_df, phase_df, phase_codename):
    if len(phase_df.index.difference(forcast_df.index)) != 0:
        raise cleaningException("The index for your submission and ground truth don't match. Expected: \n{}. \n Found: \n {}". format(forcast_df.index.to_frame(index=False), forcast_df.index.to_frame(index=False)))

def check_for_no_duplicates(forcast_df, phase_codename):
    if len(forcast_df[forcast_df.index.duplicated()]) !=0 :
        raise formatException("Your prediction has the following duplicates: \n{}".format(forcast_df[forcast_df.index.duplicated()].index.to_frame(index=False), forcast_df.index.to_frame(index=False)))

def clean_dates(forcast_df, phase_codename):
    # Check the date formatting
    if pd.to_datetime(forcast_df['Date'], format='%d-%b', errors='coerce').notnull().all():
        forcast_df['Date'] = pd.to_datetime(forcast_df['Date'], format='%d-%b', errors='raise')
    elif pd.to_datetime(forcast_df['Date'], format='%b-%d', errors='coerce').notnull().all():
        forcast_df['Date'] = pd.to_datetime(forcast_df['Date'], format='%b-%d', errors='raise')
    else:
        raise cleaningException("An error happened while parsing the dates, please contact the competition organizers.")

    if phase_codename == 'dev':
        actual_year = 2020
    elif phase_codename in ['week3', 'week4', 'feb']:
        actual_year = 2021
    else:
        raise cleaningException("An error happened while parsing phase_codename {}".format(phase_codename))
    
    forcast_df['Date'] = forcast_df['Date'].apply(lambda x: x.replace(year = actual_year))
    forcast_df.Date = pd.to_datetime(forcast_df.Date)

    return None

def clean_region_code(forcast_df, phase_codename):
    # NSW is correct for New South Wales
    if 'NWS' in forcast_df['Region'].values:
        if 'NSW' in forcast_df['Region'].values:
            raise formatException("""
                Error: Your submission contains both 'NWS' and 'NSW' in the regions column. The correct region code is 'NSW' which stands for New South Wales.
                        You must make sure that your submission denotes New South Wales with 'NSW' only and remove the 'NWS' ones.
                Note: There was a typo in the original submission guidelines that used the 'NWS' in the region codes. That was incorrect and 'NSW' is correct.""")
        else:
            print("Warning: It appears that you are using the incorrect 'NWS' for the region code. We are replacing all instances of 'NWS' with 'NSW' which denotes New South Wales.")
            print("         The correction is because there was a typo in the original submission guidelines that used the 'NWS' in the region codes. That was incorrect and 'NSW' is correct.")
            print("         Replaced {} instances of 'NWS' to 'NSW'".format(len(forcast_df[forcast_df.Region == 'NWS'])))
            forcast_df.Region[forcast_df.Region == 'NWS'] = 'NSW'
    return None


def evaluate(test_annotation_file, user_submission_file, phase_codename, **kwargs):
# def evaluate(test_annotation_file, user_submission_file, phase_codename='test', **kwargs):
    try:
        print("Evaluating for id: {}, submitted_at: {}".format(kwargs["submission_metadata"]["id"], kwargs["submission_metadata"]["submitted_at"]))
    except Exception as ex:
        print(ex)

    assert(phase_codename in CONFIG.keys())

    print("Evaluating for {} Phase".format(CONFIG[phase_codename]["name"]))

    output = {}


    actual = pd.read_csv(test_annotation_file, header=0, parse_dates=True)
    actual.Date = pd.to_datetime(actual.Date)
    actual.set_index(['Date', 'Region'], inplace=True)

    # actual = pd.read_csv(test_annotation_file).sort_values(by=['Region','Date'], ascending=True)
    
    try:
        forcast = pd.read_csv(user_submission_file, header=0, parse_dates=True)
        # forcast = pd.read_csv(user_submission_file).sort_values(by=['Region','Date'], ascending=True)
    except Exception as ex:
        raise formatException("Couldn't load your submission as a csv file. Make sure your submission is a csv file, includes the header column, and has these three columns: ['Region','Date','Estimated_fire_area']")
        # print(ex)
        # print("Couldn't load your submission as a csv file.")
        # print('Make sure your submission is a csv file, includes the header column, and has these three columns: ["Region","Date","Estimated_fire_area"]')


    check_sub_columns(forcast, phase_codename)
    check_sub_dateformat(forcast, phase_codename)
    
    clean_dates(forcast, phase_codename)
    clean_region_code(forcast, phase_codename)
    
    check_sub_region_code(forcast, phase_codename)

    forcast.set_index(['Date', 'Region'], inplace=True)
    check_for_no_duplicates(forcast, phase_codename)
    check_sub_has_all_forcasts(forcast, phase_codename)



    if (len(actual) < 5):
        print("Skipping evaluation at this time")
        output["result"] = [
            {
                CONFIG[phase_codename]["split"]: {
                    'mape': -99, 
                    'mdape': -99, 
                    'smape': -99, 
                    'smdape':-99, 
                    'maape': -99, 
                    'rmspe': -99, 
                    'rmdspe':-99, 
                    'mae': -99,
                    'rmse': -99,
                    'tot': -99
                }
            }
        ]
    else:
        # Merge
        df_merged = actual.join(forcast,lsuffix='_actual',rsuffix='_forcast')

        # Trim the df_merged to only rows available in the "actual" dataframe 
        df_merged = df_merged.loc[actual.index]

        if df_merged.isna().values.any():
            raise missingValueException("There are NA values after your forcast is joined with the actual predictions. Please check your submissions formatting again or contact the organizers if you need more help.")

        area=_evaluate(df_merged['Estimated_fire_area_actual'].to_numpy(),
                        df_merged['Estimated_fire_area_forcast'].to_numpy(),
                        metrics=('mape', 'mdape', 'smape','smdape','maape', 'rmspe', 'rmdspe','rmse', 'mae','tot'))
        output["result"] = [
            {
                CONFIG[phase_codename]["split"]: area
            }
        ]

    output["submission_result"] = output["result"][0][CONFIG[phase_codename]["split"]]
    print("Completed evaluation for {} Phase".format(
        CONFIG[phase_codename]["name"]))
    return output


if __name__ == "__main__":
    # execute only if run as a script
    s = evaluate('../annotations/actual_simplified_week_3.csv','../submission_simplified.csv',  phase_codename='week3')
    print(s)
