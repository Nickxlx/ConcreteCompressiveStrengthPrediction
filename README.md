# Dataset
```
from Notebooks import cement_data.csv
```

## About dataset
```
Concrete is the most important material in civil engineering. The
concrete compressive strength is a highly nonlinear function of age and
ingredients. These ingredients include cement, blast furnace slag, fly ash,
water, superplasticizer, coarse aggregate, and fine aggregate.

```
# Local Project Setup

So, to set this project in local we have couple of steps needed. 

1. Environment creation
2. Mongodb Account setting
3. Environment variable settings

💿 Installing
## Create a new Conda environment
```
conda create --prefix venv python==3.8 -y
```
```
conda activate /.venv
````

## MongoDb account setting

MongoDB is a popular NoSQL database that allows you to store and retrieve data in a flexible and scalable way. In this guide, we will go through the steps of creating a MongoDB account, database, and how to get the Python 3.8 client URL for MongoDB.

### Step 1: Create a MongoDB account

**To create a MongoDB account, follow these steps:**

1. Go to the MongoDB website and click on the "Sign Up" button.

2. Fill in the required details such as your name, email address, and password.

3. Verify your email address by clicking on the link sent to your email.

4. Once you have verified your email address, log in to your MongoDB account.

### Step 2: Create a MongoDB database

**To create a MongoDB database, follow these steps:**

1. Click on the "Create a Cluster" button on the MongoDB Atlas dashboard.

2. Choose the free plan by selecting the "Shared" option.

3. Choose your preferred cloud provider, region, and cluster name.

4. Click on the "Create Cluster" button.

5. Once the cluster is created, click on the "Collections" button to create a new collection in the database.

### Step 3: Get the Python 3.8 client URL

To get the Python 3.8 client URL for MongoDB, follow these steps:

1. Click on the "Connect" button on the MongoDB Atlas dashboard.

2. Select "Connect your Application".

3. Choose your preferred programming language ( for us python), version ( for us 3.6 or above), and driver.

4. Copy the Python 3.8 client URL provided.

5. Use the client URL to connect to your MongoDB database in Python.

## Final Project Run

Once you have successfully completed the steps above, 
- Install the **requirements.txt** by running the following command 

To install the dependencies
```
pip install -r requirements.txt
```
 Run Application
```
python application.py
```
## For prediction go to 
http://127.0.0.1:5000/predict

The project should run now in your local pc. 