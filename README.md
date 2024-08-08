# Context-aware predictive process monitoring for emergency department: a case study

Project in ![PyPI - Python Version](https://img.shields.io/badge/python-3.12-3776AB?logo=python)


### > Script Execution

#### ```01_log_read.py```
Loads the main event log, extracts statistics and adds duration and remaining time of each case (stardard event log with suffix ```_std```). It also creates the version of the event log with the values of the ACTIVITY column in ENG. It enriches the event log, creating the file with the suffix ```_enr```. Starting file is: /data_log/EVENT-LOG_ED.csv.  

#### ```02_log_prefix.py```
Extracts prefixes from the event log (std or enr).  

#### ```03_log_encoding.py```
Starting from prefixes, it encodes the tracks creating two events log (_std_ and _enr_).  

#### ```04_log_prediction.py```
Performs regression algorithms on encoded prefixes.  

### > Configurations
See ```config/config.yml```

### > Directories

#### config
Configuration directory with ```config.yml```.  

### data_encoding
Contains event log encoded prefixes.

### data_log
Contains the starting event log.  

### data_ml
Contains the results of the regression models.  

### data_prefix
Contains the event log prefixes.   

#### stats
Directory with event log stats.

### > Script Dependencies
See ```requirements.txt``` for the required libraries (```pip install -r requirements.txt```).  
