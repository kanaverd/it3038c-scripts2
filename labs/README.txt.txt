These 3 scripts are based on the "PSWindowsUpdate" module. To install this, run:

Install-Module -Name PSWindowsUpdate -Force

Make sure to select 'Y' to install this module after running the command. 

The first script using this module installs a windows update and force reboots the machine after it is done installing.
The second script with this module prevents a particular Windows update from installing on a machine when ran. 
The third script with this module removes a particular Windows update from the machine it is run on.