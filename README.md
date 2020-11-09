![](/images/wildfires-logo-github.png)

# Call for Code Spot Challenge for Wildfires

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

Go [here](XXX) to find more information and how to sign up for the contest. 

<a name="timeline"></a>
### Timeline

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

One of the conditions to be able to win the contest is to use an IBM Cloud Service such as [Watson Studio](https://cloud.ibm.com/catalog/services/watson-studio) or [AutoAI](https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/autoai-overview.html). You can sign up for a free trial account [here](XXX) and [these instructions](XXX) should get you up and running in no time.

<a name="data"></a>
## The data

Below a short summary of the data is given. Find more details in these [slides](https://github.com/Call-for-Code/Spot-Challenge-Wildfires/blob/main/resources/wildfire-challenge-data-introduction.pdf), [readme](XXX) and [example notebooks](https://github.com/Call-for-Code/Spot-Challenge-Wildfires/tree/main/notebooks). 

<a name="resources"></a>
## Further resources

<a name="terms"></a>
## Terms and Conditions

Please make sure you have agreed to the Participation Agreement for the Call for Code Spot Challenge for Wildfires before you start submitting to the [leaderboard](). You can find the participation agreement on the [contest landing page](http://ibm.biz/cfcsc-wildfires).

Items to keep in mind:

- No IBMers or Red Hatters can participate
- A contestant can have exactly one account on this leaderboard and can be in exactly one team
- The maximum team size is 5
- Teams must be registered on this leaderboard by January 8, 2021
- No team mergers are allowed
- IBM can restrict the number of teams competing
- There are four phases planned for the contest. IBM may change the details of the phases
- No sharing of notebooks and models privately between teams unless you make the content available to all
- The leaderboard determines the winner on March 1, 2021 or when IBM declares the contest closed
- At some point during the contest, an IBM tool such as Watson Studio or AutoAI should be used during the model development, training, etc.
- The top 5 contestants on the final leaderboard will be asked to share their notebook on Watson Studio and provide information on the tools they used as well as any other open datasets they incorporated


