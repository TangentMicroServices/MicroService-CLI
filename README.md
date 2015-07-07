# MicroService-CLI
A command line interface for interacting with Tangent MicroServices

## Setup

You need to export some environment variables. On the command, run:

```
export USERSERVICE_API_TOKEN=..
export TANGENT_PROJECT_ID=..
export TANGENT_TASK_ID=..
```

**tips:** 

* add the above environment variables to `~/.bash_profile` so you don't need to enter them in each time. 
* copy `hours.sh` to `/usr/bin`, then it will be available globally. 



TANGENT_PROJECT_ID and TANGENT_TASK_ID are only required for the bash version

### Logging hours with python: 

> Requires a tiny bit of setup, but a bit more flexible than the command line version

**Setup**

```
pip install click, requests
```

**Run it**

```
python hours.py
```

By default, hours.py will run with no arguments. You can provide custom arguments to speed up the process. To see all options available:

```
python hours.py --help
```


### Logging hours from the command line: 

> Zero requirements .. a little more bare bones


**usage:**

	sh hours.sh 

**result:**

```
sh hours.sh 
2015-06-09
-e Start hour: 8
-e Finish hour: 9
-e Comments: did some stuff
1
posting hours ...
{"id":1234,"user":1,"project_id":38,"project_task_id":50,"status":"Open","day":"2015-06-09","start_time":"08:00:00","end_time":"09:00:00","comments":"Debugging CPU spike on prod","hours":"1.00","created":"2015-06-09T07:20:16.499010Z","updated":"2015-06-09T07:20:16.499052Z","overtime":false,"tags":""}
done

```




