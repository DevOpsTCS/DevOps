#!/bin/sh -x


	echo -e "**************************************"
	echo -e "* Executes THE  FUNCTIONAL testcases form docker container *"
	echo -e "**************************************"
	#restarting the ssh service
	sudo service ssh start

	if which pybot > /dev/null; then 
  		echo "robot found"
  			localip=`hostname -I`;echo "$localip" >> test
  			lip=`cat test | awk '{print $1}'`
  		echo "get the docker container IP address",$lip  
  		echo "Passing it to the test case"  
  			sed -i 's/PLACEHOLDER/'$lip'/' dec.txt
  			grep "@{host_IP}" dec.txt
		  #Running the FT
		echo -e "**************************************"
		echo -e "* Executes the Functional testcases *"
		echo -e "**************************************"
 		 	sudo pybot -d new_FT_test dec.txt
  		#Copying the results
		echo -e "**************************************"
		echo -e "* Copying the results *"
		echo -e "**************************************"
  			cp -r new_FT_test ../.
	else
		echo "robot framework is not installed"
	fi 

