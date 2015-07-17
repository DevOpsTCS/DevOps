#!/bin/bash -x

	echo -e "**************************************"
	echo -e "* Executes The Unit testcases form docker container *"
	echo -e "**************************************"
	localip=`hostname -I`;echo "$localip" >> test
	lip=`cat test | awk '{print $1}'`
	echo "The Docker container IP address",$lip 
	echo -e "**************************************"
	echo -e "* Downloading modifying tox.ini file *"
	echo -e "**************************************"
	PWD=`pwd`
	 echo "PWD",`pwd`
#	cd /opt/devops;sudo wget -S http://10.125.176.67:81/simple/tox.ini
#	cp -f tox.ini /opt/devops/Serviceorchestration
	cd /opt/devops/Serviceorchestration
	echo -e "\n************************"
	echo -e "* Executing Unit Tests *"
	echo -e "************************"
		sudo tox --recreate
