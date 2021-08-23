# Datadog Backup File Check
Simple Datadog check to measure the age of the most recent file in hours. Used for checking and alerting on the presence of a recent backup. 


## Installation
- Copy the check script (newest_file_age.py) from this repo to `/etc/datadog-agent/check.d/newest_file_age.py`
- Copy the config file (newest_file_age.yaml) from this repo to `/etc/datadog-agent/conf.d/newest_file_age.yaml`
- Amend `newest_file_age.yaml` for the directory you would like to check
- Restart the datadog agent
```
sudo systemctl restart datadog-agent
```

- Test with:
```
sudo -u dd-agent -- datadog-agent check newest_file_age
```
- Check the Datadog UI for metrics
- Amend the check as needed if you prefer more frequent checks or checks based on seconds
- On the Datadog UI create a monitor to alert when the `newest_file_age.hours` exceeds your preferred threshold
