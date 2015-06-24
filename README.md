# safron-test

Steps to get running 

1. Clone repo
2. CD into cloned repo
3. Run $ vagrant up (download vagrant if you do not have it)
4. ssh into vagrant $ vagrant ssh
5. change into vagrant directoryL $ cd /vagrant
6. Update the vagrant machine: $ sudo apt-get update
7. Install the Storm requirements: $ sudo add-apt-repository ppa:storm/ppa
8. And: $ sudo apt-get install python-storm
9. Start the server within the vagrant directory: $ python server.py
10. Start the client within the vagrant directory on another termical screen: $ python client.py
11. Follow promts on the client terminal window
