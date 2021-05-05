[![License](https://img.shields.io/badge/License-Apache2-blue.svg)](https://www.apache.org/licenses/LICENSE-2.0) [![Community](https://img.shields.io/badge/Join-Community-blue.svg)](https://developer.ibm.com/callforcode/solutions/projects/get-started/)

![](/images/wildfires-logo-github-v2.png)

# Call for Code Spot Challenge for Wildfires

## Upcoming live events and replays

### 2021

* 11 Jan 5PM GMT: Leaderboard and refreshed data(watch the [Replay](https://www.crowdcast.io/e/call-for-code-spot-4))
* 18 Jan 5PM GMT: Hear from Team WildFireNet (watch the [Replay](https://www.crowdcast.io/e/call-for-code-spot-5))
* 25 Jan 5PM GMT: Hypothesis Testing of Multivariate Time Series (watch the [Replay](https://www.crowdcast.io/e/call-for-code-spot-6)) 
* 22 Feb 12.30pm GMT: Approaches to Building Models for the Wildfires Challenge (watch the [Replay](https://www.crowdcast.io/e/call-for-code-spot-7))

### 2020

* 23 Nov 5PM GMT: Introduction to the challenge (watch the [Replay](https://www.crowdcast.io/e/call-for-code-spot))
* 30 Nov 5PM GMT: Learn more about the data (watch the [Replay](https://www.crowdcast.io/e/call-for-code-spot-2))
* 7 Dec 5PM GMT: Learn how to use autoAI in the challenge (watch the [Replay](https://www.crowdcast.io/e/call-for-code-spot-3))

## Links

* Landing page - http://ibm.biz/cfcsc-wildfires
* GitHub repo - https://github.com/Call-for-Code/Spot-Challenge-Wildfires
* Leaderboard - http://ibm.biz/cfcsc-wildfires-lead
* Slack workspace - http://callforcode.org/slack - #cfcsc-wildfires channel

## Predicting Wildfires

- The ultimate goal of the challenge is to predict the area of wildfires in 7 regions in Australia for **February 2021** with historical wildfire and both historical and forecast weather data, so you will be predicting fires before they happened!
- The final submissions will be on **31 January 2021**.
- But until then you can work on your model with the provided data and any other open datasets that you think might be relevant.
- Before the final submission there will be three prediction submissions to first predict the wildfires in February 2020, and then for the third and fourth week of January. This will give you time to improve your model for the final submission.

## **Table of Contents**
- [**The contest**](#contest)
  - [Timeline](#timeline)
  - [Submissions](#submissions)
  - [IBM Cloud](#cloud)
- [**The data**](#data)
- [**Further resources**](#resources)
- [**Terms and Conditions**](#terms)

<a name="contest"></a>
## The contest

Go [here](http://ibm.biz/cfcsc-wildfires) to find more information and how to sign up for the contest. Below a summary is given.

**Challenge: predict the size of the fire area in km squared by region in Australia for each day in February 2021.**

To forecast the wildfires, you will be given 5 datasets, extracted from  [Weather Operations Center Geospatial Analytics](https://www.ibm.com/products/weather-operations-center/geospatial-analytics) component ([PAIRS Geoscope](https://ibmpairs.mybluemix.net/queries)), which you can augment with other open datasets. You will also be given opportunities to try out your predictions before February in earlier stages of the contest.

Note that there is no hidden data in this contest. You will be predicting  wildfires in February 2021 during January 2021. The leaderboard will check how closely your prediction matches with reality.

**The Prize**: one winner at the top of the final leaderboard on March 1, 2021 (or when IBM declares the contest closed) gets $5K.

<a name="timeline"></a>
### Timeline

There will be four main contest stages  - the first three stages are for practice. The final stage is what the contestants will be measured on. Find more details and submission dates [here](http://ibm.biz/cfcsc-wildfires). For each stage the provided data will be improved, so check back here and make sure you use the right data from [here](https://github.com/Call-for-Code/Spot-Challenge-Wildfires/tree/main/data).

* Try the platform - Predict Feb 2020
* Predict Jan 2021 week 3 (Jan 16-22)
* Predict Jan 2021 week 4 (Jan 23-29)
* Predict Feb 2021 (Feb 1-28)

<a name="submissions"></a>
### Submissions

- For each submission you need to submit a single `.csv` file
- Your `.csv` file must contain the following columns: `Region`, `Date`, `Estimated_fire_area`
  - `Region` column is formatted as a string with values: `NWS`, `NT`, `QL`, `SA`, `TA`, `VI`, `WA`
  - `Date` column is formatted as "Day-Month", for example: `1-Feb` or `10-Feb`
  - `Estimated_fire_area` column is formatted as floats
  - Your predictions must include one line per region per date. 
    - The number of lines depends on which of the rounds you are submitting to
    - For instance, you need 196 entries and the header if you are predicting February 2021 (7 regions * 28 days + header) and 49 entries and the header if you are predicting a week (7 regions * 7 days + header)
    - An example submission file is provided [here](https://github.com/Call-for-Code/Spot-Challenge-Wildfires/blob/main/data/submission-example.csv)

<a name="cloud"></a>
### IBM Cloud

One of the requirements to win the contest is to use an IBM Cloud Service such as [Watson Studio](https://cloud.ibm.com/catalog/services/watson-studio) or [AutoAI](https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/autoai-overview.html). After you sign up for a free trial account [these instructions](https://github.com/Call-for-Code/Spot-Challenge-Wildfires/blob/main/watson-studio-instructions.md) should get you up and running in no time.

In Watson Studio you can for instance run Jupyter notebooks, like [this one](https://github.com/Call-for-Code/Spot-Challenge-Wildfires/blob/main/notebooks/wildfire-data-introduction.ipynb). Or use AutoAI to build your model for which these [instructions](https://github.com/Call-for-Code/Spot-Challenge-Wildfires/blob/main/resources/AutoAI_WalkThrough_NSW_Temperature_Data.pdf) will get you started. 

<a name="data"></a>
## The data

**All resources in this repo are described [here](https://github.com/Call-for-Code/Spot-Challenge-Wildfires/blob/main/content.md).**

Data is provided as a [zip file](https://github.com/Call-for-Code/Spot-Challenge-Wildfires/tree/main/data) that contains the below files. **For each submission round a new zip file will be added, make sure you use the right one!**

The following data is provided as daily timeseries for the 9 regions:

* Historical wildfires
* Historical weather
* Historical weather forecasts
* Historical vegetation index
* Land classes (static throughout the contest)

Find details about the data sources and data processesing [here](https://github.com/Call-for-Code/Spot-Challenge-Wildfires/blob/main/content.md), and in these [slides](https://github.com/Call-for-Code/Spot-Challenge-Wildfires/blob/main/resources/wildfire-challenge-data-introduction.pdf) and the [data documentation](https://github.com/Call-for-Code/Spot-Challenge-Wildfires/blob/main/data/Readme_Docs_Wildfires-Datasets_2020-11.pdf). 

This [Jupyter notebook](https://github.com/Call-for-Code/Spot-Challenge-Wildfires/blob/main/notebooks/wildfire-data-introduction.ipynb) will you get started with loading and exploring the data. The data can be loaded directly from this repository into a notebook:

```python
!wget -N https://raw.githubusercontent.com/Call-for-Code/Spot-Challenge-Wildfires/main/data/Nov_10.zip
zip = zipfile.ZipFile("Nov_10.zip")
zip.extractall()
```

<a name="resources"></a>
## Further resources

* [Forecasting - principles and practice](https://otexts.com/fpp2/) - online textbook on forecasting
* [Prophet](https://facebook.github.io/prophet/) - forecasting toolbox from Facebook

<a name="terms"></a>
## Terms and Conditions

Please make sure you have agreed to the Participation Agreement for the Call for Code Spot Challenge for Wildfires before you start submitting to the [leaderboard](http://ibm.biz/cfcsc-wildfires-lead). You can find the participation agreement on the [contest landing page](http://ibm.biz/cfcsc-wildfires).

Items to keep in mind:

- No IBMers or Red Hatters can participate
- A contestant can have exactly one account on this leaderboard and can be in exactly one team
- The maximum team size is 5
- Teams must be registered on this leaderboard by January 30, 2021
- No team mergers are allowed
- IBM can restrict the number of teams competing
- No sharing of notebooks and models privately between teams unless you make the content available to all
- The leaderboard determines the winner on March 1, 2021 or when IBM declares the contest closed
- At some point during the contest, an IBM tool such as Watson Studio or AutoAI should be used during the model development, training, etc.
- The top 5 contestants on the final leaderboard will be asked to share their notebook on Watson Studio and provide information on the tools they used as well as any other open datasets they incorporated


