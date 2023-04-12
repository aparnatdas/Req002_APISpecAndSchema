# Req002_APISpecAndSchema
Requirement 002 - For API Spec and Schema

Python Behave provides us a BDD(Behavior Driver Development), python style

Behavior-driven development (or BDD) is an agile software development technique that encourages collaboration between developers, QA and non-technical or business participants in a software project.

Behave uses tests written in a natural language style, backed up by Python code.

First, install behave. (pip install behave)

Now make a directory called "features/". In that directory create a file called "get_request.feature" containing:
![image](https://user-images.githubusercontent.com/10363367/231385595-c76ae599-59ce-4417-880e-6294455f6466.png)

Make a new directory called "features/steps/". In that directory create a file called "output_file_validation.py" containing: Every Given, When and Then should be covered

![image](https://user-images.githubusercontent.com/10363367/231386155-f21e4f8e-91c5-4574-a3ea-389a61ddf582.png)

Run Behave

We can run behave with simple $behave or using the following command <Project_Dir>\features --no-capture

Run/Debug Configurations

![image](https://user-images.githubusercontent.com/10363367/231386327-99f8579d-3dc9-4363-9eb9-32cbac8e6184.png)


Allure Reports are used for Reporting

Local reports can be generated with the following command "behave -f allure_behave.formatter:AllureFormatter -o my_allure"

Allure reports can be hosted by "allure serve my_allure"

Allure Report

![image](https://user-images.githubusercontent.com/10363367/231386485-e59c317c-1b6b-4d33-a1be-b3b089462f68.png)

