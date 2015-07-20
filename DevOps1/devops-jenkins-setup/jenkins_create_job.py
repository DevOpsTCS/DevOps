import jenkins
import config
from distutils.dir_util import copy_tree

def createJenkinsJob(jobName):
    j = jenkins.Jenkins('http://10.125.155.107:9090') #ip which has jenkins up and running
    file1=open("/home/tcs/shalini-workspace/devops-jenkins-setup/jobs/"+jobName+".xml") #to get the xml file from the jobs folder
    xmlStr=''
    file2=reduce(lambda x,y:x+y,file1)
    xmlStr=str(file2)
    j.create_job(jobName, xmlStr)
    j.enable_job(jobName)


def main():
    jobList=config.jobList
    for i,x in enumerate(jobList):
        if x == 1:
            createJenkinsJob(config.jobNameList[i]) # calls create job for the job which has value 1.

if __name__ == "__main__": main()

#j.reconfig_job('test1', xmlStr)
#last_build_number = j.get_job_info('dockertest')['lastCompletedBuild']['number']
#build_info = j.get_job_info('dockertest', last_build_number)
#print(build_info)
#j.delete_job('test1')
