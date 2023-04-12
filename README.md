# Req002_APISpecAndSchema
Requirement 002 - For API Spec and Schema

Python Behave provides us a BDD(Behavior Driver Development), python style

Behavior-driven development (or BDD) is an agile software development technique that encourages collaboration between developers, QA and non-technical or business participants in a software project.

Behave uses tests written in a natural language style, backed up by Python code.

First, install behave. (pip install behave)

Now make a directory called "features/". In that directory create a file called "example.feature" containing:
![image](https://user-images.githubusercontent.com/10363367/231387057-542ec792-9931-4350-813a-00c557f5d262.png)

Make a new directory called "features/steps/". In that directory create a file called "example.py" containing: Every Given, When and Then should be covered

![image](https://user-images.githubusercontent.com/10363367/231387149-a9b0f480-73a8-4018-93d2-f73a1cc8d61b.png)

Run Behave

We can run behave with simple $behave or using the following command <Project_Dir>\features --no-capture

Run/Debug Configurations

![image](https://user-images.githubusercontent.com/10363367/231386327-99f8579d-3dc9-4363-9eb9-32cbac8e6184.png)


Allure Reports are used for Reporting

Local reports can be generated with the following command "behave -f allure_behave.formatter:AllureFormatter -o my_allure"

Allure reports can be hosted by "allure serve my_allure"

Allure Report

![image](https://user-images.githubusercontent.com/10363367/231386485-e59c317c-1b6b-4d33-a1be-b3b089462f68.png)

