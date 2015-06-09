import click, requests, json, os
from datetime import date

project_service = "http://projectservice.tangentmicroservices.com/api/v1"
me_url = "http://userservice.tangentmicroservices.com/api/v1/users/me/"


token = os.environ['USERSERVICE_API_TOKEN']
headers = {
        'content-type': 'application/json',
        'Authorization': 'Token {0}' . format(token)
    }

def me(*args, **kwargs):

    response = requests.get(me_url, headers=headers)

    j = json.loads(response.content)
    print "Hi {0} :) " . format(j.get('first_name'))
    return j.get('id')

def projects(*args, **kwargs):
    
    
    url = "{0}/projects/" . format (project_service)
    
    response = requests.get(url, headers=headers)
    
    projs = json.loads(response.content)
    for p in projs:
        print "({0}) {1}" . format (p.get("pk"), p.get("title"))
        for task in p.get("task_set", []):
            print "\t({0}) {1}" . format (task.get("id"), task.get("title"))

    project = click.prompt('Which project (number)')
    task = click.prompt('Which task (number)')

    return (project, task)


if __name__ == '__main__':
    
    user = me()

    start = int(click.prompt('Start hour'))
    stop = int(click.prompt('Stop hour'))

    project, task = projects()
    comments = click.prompt('Comments:')

    hours = stop - start
    date = date.today().isoformat()
    
    data = {"user":user,
            "project_id":project,
            "project_task_id":task,
            "start_time":"{0}:00:00" . format (start),
            "end_time":"{0}:00:00" . format (stop),
            "hours":hours,
            "day":date,
            "comments":comments
    }

    url = 'http://hoursservice.tangentmicroservices.com/api/v1/entry/'

    response = requests.post(url, data=json.dumps(data), headers=headers)
    if response.status_code == 201:
        print "\o/ got them hours"
    else:
        print "ERRROROROROR"
        print response.content


