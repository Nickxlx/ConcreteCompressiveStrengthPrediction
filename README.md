# Local Project Setup: Concrete Compressive Strength Prediction

## Overview
This project involves predicting the compressive strength of concrete based on its ingredients and age. Concrete compressive strength is a crucial factor in civil engineering, and it is influenced by several non-linear factors, including the type and quantity of materials used (cement, blast furnace slag, fly ash, water, superplasticizer, coarse aggregate, and fine aggregate). The dataset for this project is available in the file `cement_data.csv`.

## Prerequisites

### 1. Environment Setup
Creating a dedicated environment ensures that all dependencies are isolated, reducing conflicts with other projects.

**Step 1: Create a new Conda environment**

Execute the following command to create a new Conda environment with Python 3.8:
```bash
conda create --prefix ./venv python=3.8 -y
```

**Step 2: Activate the Conda environment**

Once the environment is created, activate it using:
```bash
conda activate ./venv
```

### 2. MongoDB Account Setup
MongoDB is used as the database for storing and managing data. Below are the steps to set up MongoDB.

**Step 1: Create a MongoDB Account**

1. Visit the [MongoDB website](https://www.mongodb.com/) and click on "Sign Up."
2. Complete the registration form with your name, email, and password.
3. Verify your email address by clicking on the verification link sent to your inbox.
4. After verification, log in to your MongoDB account.

**Step 2: Create a MongoDB Database**

1. On the MongoDB Atlas dashboard, click "Create a Cluster."
2. Select the "Shared" option to choose the free tier.
3. Choose your preferred cloud provider, region, and give your cluster a name.
4. Click "Create Cluster" and wait for it to be provisioned.
5. Once your cluster is ready, click "Collections" to create a new collection in your database.

**Step 3: Obtain the Python Client URL**

1. In the MongoDB Atlas dashboard, click on "Connect."
2. Choose "Connect your Application."
3. Select Python as your preferred programming language and ensure the version is 3.6 or above.
4. Copy the provided Python connection URL.

You will use this URL to connect your Python application to MongoDB.

### 3. Environment Variable Configuration
Ensure your MongoDB credentials and other sensitive information are securely managed using environment variables. For example:

1. Create a `.env` file in the root of your project.
2. Add your MongoDB connection string and other variables:
   ```
   MONGO_URI=your_mongodb_connection_string
   ```

### 4. Installing Project Dependencies
With the environment set up and MongoDB configured, install the necessary dependencies for the project.

**Step 1: Install dependencies**

Ensure you are in your activated Conda environment, then run:
```bash
pip install -r requirements.txt
```

### 5. Running the Application
Once all dependencies are installed, you can run the application.

**Step 1: Start the application**

Run the following command:
```bash
python application.py
```

**Step 2: Access the prediction service**

Open your browser and navigate to:
```
http://127.0.0.1:5000/predict
```
This will take you to the prediction interface, where you can input data and receive predictions on concrete compressive strength.

---
