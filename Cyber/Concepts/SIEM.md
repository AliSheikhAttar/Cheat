SIEM: SIEM systems are products (typically software) that allow you to monitor security information and events.

SIEM systems can do:

- Log aggregation: Log files are collected from multiple systems and network devices into the SIEM software so that they can be analyzed from a single location.
- Correlation: SIEM software has the capabilities to compare events from different log files in order to link those events together as security-related events.
- Automated alerting and triggers: Alerts are triggered and sent out based on events configured by the administrator that occur within the log files.

- Time synchronization: The SIEM software can ensure that the time is synchronized across devices so that security events across devices are recorded at the same time.
- Event deduplication: The SIEM system can trim event logging so that the same event is not recorded over and over again, filling up the log space.
- Logs/WORM: When writing to log files, the SIEM system uses a write-once, read-many (WORM) approach, where the log entry is written once but can be read many times.

## Vendors SEIM
- Splunk SIEM
- IBM Security QRadar
- Micro Focus ArcSight
- LogRhythm
- Elastic Search
- SolarWinds SIEM
- Datadog
- EventTracker
- Securonix
- Rapid7

## SOAR 
can be used by companies to collect security event data from different sources, detect a security threat, and then automate a response to the threat to take some form of corrective action.

We can automate our security operations with three main areas of focus:

Threat and vulnerability management
Security incident response
Security operations automation"