# To install and run this script on Ubuntu 20.04 in a screen session, follow these steps:

### 1. Install Python 3, pip and screen on your Ubuntu 20.04 system:
<code>sudo apt update -y && sudo apt install python3-pip -y && sudo apt install screen -y
</code>

### 2. Install the required Python packages using pip:
<code>pip install httpx</code>

### 3. Copy the script to your Ubuntu 20.04 system.

### 4. Create a screen session by typing the following command:

<code>screen -S shardeum-node-restarter python3 ./shardeum_restarter.py -p YOUR DASHBOARD PASSWORD</code>

Detach from the screen session by pressing Ctrl+a followed by d. This will leave the screen session running in the background.

To reattach to the screen session at any time, type the following command:
<code>screen -r shardeum-node-restarter</code>
