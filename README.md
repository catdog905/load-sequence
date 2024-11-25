# Utility for Load Testing Service

The main function of the utility is to simulate client interactions with a service. The utility generates a specified number of clients and runs a scenario for each client in a separate thread. It supports different scenarios for testing various service interactions. Each scenario consists of steps, each of which corresponds to a request to the service. Previously obtained data can be used within the scenario. New scenarios can be added declaratively without requiring substantial changes to the code. During the load testing process, Locust collects metrics on the responsiveness of the service, which can later be exported to a separate CSV file.

## Instructions for Running the Utility

### Using Docker

Build the Docker image:

```bash
docker build . -t load-sequence
```

Run the utility:
```bash
docker run -p 8089:8089 load-sequence locust -f llocustfiles/test_scenario.py
```

After starting, the control panel can be accessed at localhost:8089. Here, you can set the required number of users and the rate of user growth from zero to the desired value. The panel allows you to monitor the metrics and the overall testing process. You can also download the final testing results from there.

### Manually

First, create a Python virtual environment. I used Python 3.12.3.

```bash
python3 -m venv venv
```
A new folder `venv` will be created.

Activate the virtual environment with the following command:

```bash
source venv/bin/activate
```
for Linux

```bash
venv\Scripts\activate.bat
```
for Windows

Activating the Python virtual environment will change the environment variables of the current terminal, redirecting commands like `python`, `pip`, and others to the `venv` folder. Therefore, all subsequent commands should be executed in the terminal with the environment activated.

Next, install the dependencies:
```bash
pip install -r requirements.txt
```

If the virtual environment was activated, the packages will be installed into the newly created `venv` folder.

To run the utility, use the following command and specify the configuration 

Locust file:
```bash
locust -f locustfiles/test_scenario.py
```

After starting, the control panel can be accessed at `localhost:8089`. Here, you can set the required number of users and the rate of user growth from zero to the desired value. The panel allows you to monitor the metrics and the overall testing process. You can also download the final testing results from there.


## Project Structure

|                    |      |
|--------------------|------|
| locustfiles        | Configurations for different load testing scenarios |
| sequence           | Implementation of action sequences |
| \| action          | Templates for various actions |
| \| \| http         | HTTP request templates |
| main.py            | Executable file for testing a single load testing scenario |
| requirements.txt   | List of dependencies for running the utility |