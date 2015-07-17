'''orginal_path="/home/tcs/DEVOPS/original_iso"
repo_path="/home/tcs/DEVOPS/repo_iso"
IPA_file="/home/tcs/DEVOPS/vm_ipaddress"

password="tcs@12345"
username="tcs"
vm_name="image-processor"
orig_disk_name="ubuntu_compressed.qcow2"
disk_name="devops-build-11"
_bridge='br0'
host_subnet="10.127.150.0/24"
git_user="root"
git_password="test12345"
gerrit_user="madhavi"
git_ip="10.125.155.98"
gerrit_port="8090"
git_repo="Serviceorchestration"
pip_repo="http://10.125.176.67/simple"
repo_opt="git"
kill="yes"
db_template="/home/tcs/DEVOPS/devops.sql.template"
db_url_template="/home/tcs/DEVOPS/devops.sql.url.template"
db_file="/home/tcs/DEVOPS/devops.sql"'''

#jobs execution
test1=1
GERRIT_TRIGGER_SO_config=0
TEST_EXECUTION_FT_SO_config=0
GITSYNC_SO_config=0
IMAGECREATION_config=0

jobList=[test1,GERRIT_TRIGGER_SO_config,TEST_EXECUTION_FT_SO_config,GITSYNC_SO_config,IMAGECREATION_config]
jobNameList=["test1","GERRIT_TRIGGER_SO_config","TEST_EXECUTION_FT_SO_config","GITSYNC_SO_config", "IMAGECREATION_config"]

