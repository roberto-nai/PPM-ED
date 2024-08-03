# Context-aware predictive process monitoring for emergency department: a case study

Project in ![PyPI - Python Version](https://img.shields.io/badge/python-3.12-3776AB?logo=python)


### > Script Execution

#### ```01_log_read.py```
Loads the main event log, extracts statistics and adds duration and remaining time of each case.  

#### ```02_log_prefix.py```
Extracts prefixes from the main event log.  

#### ```03_log_encoding.py```
Starting from prefixes, it encodes the tracks.  

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
