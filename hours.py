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

def get_date(d, m, y):

    dt = date.today()
        
    if None not in [d, m, y]:
        dt = date(year=y, month=m, day=d)
        print "Setting hours for: {0}" . format (dt.isoformat())

    return dt.isoformat()

@click.command()
@click.option('--d', default=None, type=click.IntRange(1, 31), help='The day to capture time for in the format dd.')
@click.option('--m', default=None, type=click.IntRange(1, 12),  help='The month to capture time for in the format mm.')
@click.option('--y', default=None, type=click.INT, help='The year to capture time for in the format yyyy.')
@click.option('--start', default=None, type=click.IntRange(0, 24), help='The 24hour time that you started working.')
@click.option('--stop', default=None, type=click.IntRange(0, 24), help='The 24hour time that you stopped working.')
@click.option('--project', default=None, type=click.INT, help='The ID of the project you\'re logging time for.')
@click.option('--task', default=None, type=click.INT, help='The ID of the task you\'re logging time for.')
@click.option('--comments', default=None, help='Some detail on what work you were doing.')
def run(d, m, y, start, stop, project, task, comments, *args, **kwargs):
    
    date = get_date(d, m, y)    
    user = me()

    if start is None: 
        start = int(click.prompt('Start hour'))
    
    if stop is None:
        stop = int(click.prompt('Stop hour'))

    if None in [project, task]:
        project, task = projects()
    
    if comments is None:
        comments = click.prompt('Comments')

    hours = stop - start
    
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

if __name__ == '__main__':
    run()


