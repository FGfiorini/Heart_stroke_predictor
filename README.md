# Credits

Front end developed by:
Leandro Martinez, Github: https://github.com/leandroMz
Javier Coll, Github: https://github.com/JaviiColl

API developed by Franco J. G. Fiorini

# Disclaimer

This is a project only for research and academic purposes. The aim of this is just to show how I worked and developed an API. If you have any kind of health condition it's mandatory to get medical consultation.



# Flask ML API

A flask API developed with a form in the frontend. Used for a Heart stroke prediction analysis project where the goal is to predict whether a person could have possibly a heart stroke or not, based on data provided through the form. The target value considered is 1, possibly heart stroke. Label = 0, healthy heart. 
Its composed by three microservices, that are configured to be excecuted with a docker compose yml file:

- API
- Redis
- ML Service


# Project structure 

Below is the full project structure:

```
├── api
│   └── static
│   │      ├── images
│   │      └── style
│   ├── templates
│   ├── _init_.py
│   ├── app.py
│   ├── Dockerfile
│   ├── settings.py
│   ├── middleware.py
│   ├── requirements
│   └── views.py
├── model
│   ├── preprocess
│   |       ├── data
|   |       ├── Dockerfile
|   |       ├── preprocess.py
│   |       └──requirements
│   |       
│   |       
|   ├── Training
│   |       ├── pickles
|   |       ├── Dockerfile
│   |       ├── requirements
│   |       └── train.py
|   |       
│   ├── _init_.py
│   ├── Dockerfile
│   ├── ml_service.py
│   ├── preprocess.py
│   ├── requirements
│   └── settings.py
│   
├── notebooks
│   ├── EDA.ipynb
│   └── Feature Enguneering and Model Evaluation
├── gitignore
├── docker-compose.yml
├── Model Evaluation report.md
└── README.md
```

A quick overview on each module:

- api: It has all the needed code to implement the communication interface between the users and our service. It uses Flask and Redis to queue tasks to be processed by our machine learning model.
    - `api/app.py`: Setup and launch our Flask api.
    - `api/views.py`: Contains the API endpoints. 
    - `api/settings.py`: It has all the API settings.
    - `api/templates`: Here we put the .html files used in the frontend.
    - `api/middleware`: It has a function that queues jobs into redis and waits for ML model to get a prediction as answer.

- model: Implements the logic to get jobs from Redis and process them with our Machine Learning model. When we get the predicted value from our model, we must encole it on Redis again so it can be delivered to the user.
    - `model/Trainig/pickles`: Here I saved pickle files that will be rehused in other scripts of the project. 
    - `model/ml_service.py`: Contains functions to get prediction and probability with our ML model, and save the results in redis.
    - `model/preprocess/preprocess.py`: Here we gouped all feature engineering in a single pipeline as to be reused later in the project.
    - `model/preprocess/settings.py`: It has the API settings and some definition of variables.
    - `model/Trainig/train.py`: Here I train the selected model.
    - `model/preprocess/utils.py`: Implements some extra functions used for the data preprocess.
    - `data`: Here we saved the raw data to start the project.
- notebooks: Here we have the notebooks where we started with the project doing the EDA and training models.
    - `notebooks/EDA.ipynb`: Notebook where we made feature engineering.
    - `notebooks/Feature Engineering and Model Evaluation.ipynb`: Here we trained some models and got their metrics.
- uploads: Here saves the forms.csv file were all the completed forms data is saved. 


# Steps to run all the project:

1. save in data directory, inside model/preprocess/data, your csv or txt file with raw data
2. create a container - docker image build -t prepro:0.0.1 "path-to-preprocess-folder"
3. run the container - docker run -v "path-to-Training-folder"/pickles:/src/pickles prepro:0.0.1
4. create the next container - docker image build -t train:0.0.1 "path-to-Training-folder"
5. run the container - docker run -v "path-to-Training-folder"/pickles:/src/pickles train:0.0.1
6. run docker-compose.yml file
7. go to the browser "localhost"
8. fill the form displayed in frontend and summit to obtain results


## How to build and run

To run the services using compose:

```bash
$ docker-compose up --build -d
```

To stop the services:

```bash
$ docker-compose down
```


# The form

You must complete each field on the form as to make predictions of the class and probability asociated.
