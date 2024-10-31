# AppAdress
AppAdress is a Python application designed to monitor active network connections of specified programs.

## Features
- Network Connection List: Displays the current network connections of the specified program with IP addresses and port information.
- Real-Time Monitoring: Allows real-time monitoring by updating connection data every 5 seconds.
- Active Process Display: Provides a list of active programs on the system, making it easy to determine which applications are running.
## Use Cases
- System Management: Monitor network traffic to identify potential security threats.
- Security Analysis: Monitor network connections of specific apps to prevent data leaks.
## How to Use
When you run the application, you will see a list of programs accessing your network. Enter the name of the program you want to monitor. The application will then update every 5 seconds and show the servers to which the specified application is connected, along with the ports used.

- LADDR: Your IP address and port information.
- RADDR: IP address and port information of the monitored application. 
<br>
<br>
Data presented in the same row are associated links.

## Required Libraries
- psutil
- time
- requests

<hr>

<i>I welcome feedback and ideas for further development.<i>
