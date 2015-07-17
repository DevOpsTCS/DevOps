import jenkins
import config
from distutils.dir_util import copy_tree

def createJenkinsJob(jobName):
    j = jenkins.Jenkins('http://10.125.155.202:9090')
    file1=open("/home/tcs/shalini-workspace/devops-setup/jobs/"+jobName+".xml")
    #print file1
    xmlStr=''
    file2=reduce(lambda x,y:x+y,file1)
    xmlStr=str(file2)
    j.create_job(jobName, xmlStr)
    j.enable_job(jobName)


def copyPlugins():
    src="/home/tcs/shalini-workspace/devops-setup/plugins"
    dest="/var/lib/jenkins/plugins"
    #try:
    copy_tree(src, dest)
    '''except OSError as e:
        # If the error was caused because the source wasn't a directory
        if e.errno == errno.ENOTDIR:
             shutil.copy(src, dst)
        else:
             print('Directory not copied. Error: %s' % e)'''


def main():
    copyPlugins()
    jobList=config.jobList
    for i,x in enumerate(jobList):
        if x == 1:
            createJenkinsJob(config.jobNameList[i])

if __name__ == "__main__": main()

#j.reconfig_job('test1', xmlStr)
#last_build_number = j.get_job_info('dockertest')['lastCompletedBuild']['number']
#build_info = j.get_job_info('dockertest', last_build_number)
#print(build_info)
#j.delete_job('test1')
