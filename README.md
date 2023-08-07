# Server-Monitoring-System
Computer Networks Assignment

The project aims to develop a server monitoring system using Python, allowing users to check the connectivity status of multiple servers. The system defines a Server class with attributes representing server details such as name, port, connection type (plain or SSL), and priority. The system periodically checks the servers' connectivity using various methods, including establishing plain or SSL connections and pinging the servers. The connection status, success, and timestamp are recorded and stored in a history list for each server. The history list has a maximum capacity of 100 entries, ensuring recent connection events are retained.

The system provides flexibility in monitoring both SSL and plain connections, as well as support for different operating systems by adapting the ping method accordingly. Additionally, it features an alert mechanism to notify users when a server's connection status changes, which can be critical for timely response to connectivity issues. To ensure seamless access to historical data, the system employs the pickle module to serialize the server objects and save them to a file, preserving valuable monitoring history even after system restarts.

Overall, the developed server monitoring system provides an efficient and user-friendly solution for monitoring the connectivity status of multiple servers, facilitating prompt response to connectivity problems and enabling historical analysis of server performance and stability.
