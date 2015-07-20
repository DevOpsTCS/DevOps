#!/usr/bin/python


from redmine import Redmine

import argparse

parser = argparse.ArgumentParser(description='Short sample app')

parser.add_argument('--description',default="")
parser.add_argument('--projectid',default="Devops")
parser.add_argument('--subject',default="NSD Service is not available")
parser.add_argument('--tracker_id',default="3")
parser.add_argument('--status_id',default="1")

myargs=parser.parse_args()
desc=str(myargs.description)
projectid=myargs.projectid
sub=myargs.subject
trid=int(myargs.tracker_id)
status=int(myargs.status_id)

redmine = Redmine('http://10.125.155.220/redmine', username='admin', password='admin')
#import pdb;pdb.set_trace()
#projects = redmine.project.all()
#issues = redmine.issue.all(sort='category:desc')
#print issues

#print projects

issue = redmine.issue.create(project_id=projectid, subject=sub, tracker_id=trid, description=desc, status_id=status, priority_id=2, assigned_to_id=4, watcher_user_ids=[5,6,7],start_date='2015-06-19', due_date='2015-06-19', estimated_hours=4)
