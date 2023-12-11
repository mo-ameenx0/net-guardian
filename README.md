# NetGuardian

NetGuardian is a network packet anomaly detection framework and GUI based on the
[UNSW-NB15](https://www.kaggle.com/datasets/mrwellsdavid/unsw-nb15) dataset. The
framework works as the backend for the GUI application. The GUI allows the uesr to
test multiple models combinations and feature selection in a user frindly manner.

In addition, the application can seamlessly integrate with different datasets.
It also offers the flexibility to easily incorporate new machine learning or
deep learning models and allows the combination of multiple models.

# Application Build Steps

**_Note: the application was developed using linux operating system_**

To build the application and install into your system follow the steps:

1. Open a terminal and then go to the project folder

2. Build the python package.
   ```
   ~$ python -m build
   ```

# Application Development Steps

**_Note: the application was developed using linux operating system_**

To start developing and testing the application follow the steps:

1. Create a python virtual enviroment

   ```
   ~$ python -m venv .venv
   ```

2. Activate the virtual enviroment

   ```
   ~$ source .venv/bin/activate
   ```

3. Install the package into the virtual enviroment

   ```
   ~$ pip install --editable .
   ```

4. Install requried packages

   ```
   ~$ pip install -r requirements.txt
   ```

5. Run the AutoNation application and start the development
   ```
   ~$ NetGuardianGUI
   ```
