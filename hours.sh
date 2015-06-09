#!/bin/bash

# default:
date=`date +%Y-%m-%d`
echo $date
echo -e "Start hour: \c "
read  start

echo -e "Finish hour: \c "
read  end

echo -e "Comments: \c" 
read comments 

hours=$((end-start))

echo $hours

echo "posting hours ..."
curl 'http://hoursservice.tangentmicroservices.com/api/v1/entry/' \
-H 'Content-Type: application/json;charset=UTF-8' \
-H 'Accept: application/json, text/plain, */*' \
-H 'Authorization: Token '"$USERSERVICE_API_TOKEN"'' \
--data '{"user":1,"project_id":'"$TANGENT_PROJECT_ID"',"project_task_id":'"$TANGENT_TASK_ID"',"status":"Open","start_time":"'"$start"':00:00","end_time":"'"$end"':00:00","hours":"'"$hours"'","day":"'"$date"'","comments":"'"$comments"'"}'

#--data '{"user":1,"project_id":38,"project_task_id":50,"status":"Open","start_time":"'"$start"':00:00","end_time":"'"$end"':00:00","hours":"'"$hours"'","day":"'"$date"'","comments":"'"$comments"'"}'

echo "done"
