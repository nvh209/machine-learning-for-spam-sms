# Cellular Network Simulation

The cellular network simulation is a simulation of a cellular network with a focus on the SMS spam detection [Simulation File](../simulation/simulation.ipynb). The simulation is based on the [SMS Spam Collection Dataset](https://www.kaggle.com/uciml/sms-spam-collection-dataset) from Kaggle.

The simulation is designed to simulate the flow of SMS messages through a cellular network. The simulation consists of several network devices, including mobile devices, radio units, baseband units, and a core network. The simulation also includes a spam classification model that is used to detect spam messages within the network.

The simulation is set up in the jupyter notebook with the logging function, the network device classes and other functions needed for the network simulation. The simulation is run for the entire set of SMS messages. The model results are saved in a txt file, as well as the regular logs and alert logs both saved as csv files.

## Simulations for Each Model

Each model has the same set up, the only difference is the model used. The model is trained on the training data and then tested on the test data. The model is then used to predict the SMS messages in the simulation. The simulation is then run and the results are stored in a dictionary. The results are then plotted to show the accuracy of the model.

### Data Paths

The data paths are set up for the simulation files, as part of the simulation the models created in the [models](../models/models.ipynb) are used within the simulation. The folders within the simulation for saving the results are also created.

- [SMS Spam Datasets](../simulation/data) contains the SMS Spam datasets used in the simulation.
- [Simulation Results](../simulation/results) contains the results of the simulation.
- [Simulation Logs](../simulation/logs) contains the logs of the simulation.

## Network Logging

The key feature of the simulation is the logging of the network. The network is logged at each time step, the logs are saved in the [Simulation Logs](./simulation/logs) folder. The logs are saved in the format of a CSV file.

- The regular logs contain the following information:
    - Time: The time step of the simulation.
    - Log Level: The level of the log.
    - Log Message: The message of the log.
    - SMS Content: The content of the SMS.
- The Alert Level logs contain the following information:
    - Time: The time step of the simulation.
    - Alert Level: The level of the alert.
    - Alert Message: The message of the alert.
    - Baseband Unit: The location of the baseband unit that generated the alert.
    - Spam Volume: The volume of spam messages detected.

## Data Preprocessing

- The load sms data function is similar to what was used within the model training. Here the count verctorizer created during model creation is used to transform the SMS data into a format that can be used within the simulation. The text data is transformed to be used within the simulation.
- The text data undergoes preprocessing, where various patterns such as email addresses, URLs, phone numbers, currency symbols, and digits are replaced with specific tokens ('emailaddr', 'httpaddr', 'phonenumbr', 'moneysymb', 'numbr'). Furthermore, non-alphanumeric characters are removed, and the text is converted to lowercase.

### Network Device Classes

The network device classes are created to simulate the network devices within the cellular network.

**MobileDevice class:**

- Responsible for simulating the sending of SMS messages from mobile devices.
- The `send_sms` function orchestrates the transmission of SMS messages to the baseband unit at varying intervals.
- Logs each message sent, including details like the content and timing of the transmission.

**RadioUnit class:**

- Handles the reception of SMS messages from the mobile device.
- The `process` method simulates the delay and processing of the messages before forwarding them to the next unit.
- The `process` function also Logs the receipt and processing times of messages.

**BasebandUnit class:**

- Acts as the network's traffic cop, analysing SMS content to identify spam messages.
- The `dynamic_capacity` method adjusts the processing capacity of the unit based on the time of day.
- The `process` method processes the message and classifies it as spam or ham, based on the content.
- The `process` function also Logs the receipt and processing times of messages. It also logs the classification of the message as spam or ham.
- The `check_spam_ratio` method evaluates the spam ratio and issues alerts if spam activity is above a designated threshold.
- The `evaluate_model` method evaluates the performance of the spam classification model.

**CoreNetwork class:**

- Receives processed messages from the BasebandUnit and forwards them to the mobile device.
- The `process` method simulates the delay and processing of the messages before forwarding them to the mobile device.

**ToMobileDevice class:**

- Receives the processed message thats gone over the network.
- The `process` method checks if the prediction of whether the message was ham or spam is correct. It logs the message received and stores the predicted/actual results.
  
**NetworkController class:**

- Manages the overall simulation environment and orchestrates the interactions between different network components.
- The `NetworkController` enumerates over a set amount of baseband units that are later defined. Each `BasebandUnit` is created and added to the network with it's own 2 `RadioUnit` units.
- The `evaluate_all_basebands` method evaluates the performance of the ML model in each BasebandUnit in the network.
- The `save_evaluation_results` method saves the evaluation results to a CSV file.

### Simulation Run-Time Functions

The simulation run-time functions are created to simulate the network devices within the cellular network.

**load_data:**

- Loads the SMS spam dataset and preprocesses the data for use in the simulation.
- The function returns the preprocessed SMS data and the count vectorizer used to transform the data.

**run_simulation:**

- Initialises the network controller and runs the simulation for the duration of all SMS messages.
- Sets up the logs for the simulation.

**evaluate_and_save_results:**

- Evaluates the performance of the spam classification model in each baseband unit.
- Saves the evaluation results to a txt file.

The data sets are loaded for the set number of baseband units that are to be simulated. The load data function sets up all the SMS messages from the datasets created and stored in the [SMS Spam Datasets](../simulation/data). The data is then preprocessed to be used in the simulation, this step is done prior to the actual simulation to use the same set up for each model.

## Logistic Regression Model Simulation

The logistic Regression Model is run within the simulated network with the model results saved to the folder [LR Models](../simulation/results/LR). The logs are saved in the [Simulation Logs](../simulation/logs/LR) folder. With the results visualised in the simulation. A sample of the normal logs has been added into the log files, for the full log you will need to run the simulation yourself.

- The LR model took 8m and 47s to run the simulation.

```txt
Test set accuracy: 0.88
Confusion Matrix:
 [[78879   121]
 [12266 14454]]
Classification Report:
               precision    recall  f1-score   support

         Ham       0.87      1.00      0.93     79000
        Spam       0.99      0.54      0.70     26720

    accuracy                           0.88    105720
   macro avg       0.93      0.77      0.81    105720
weighted avg       0.90      0.88      0.87    105720
```

## Naive Bayes Model Simulation

The Naive Bayes Model is run within the simulated network with the model results saved to the folder [NB Models](../simulation/results/NB). The logs are saved in the [Simulation Logs](../simulation/logs/NB) folder. With the results visualised in the simulation. A sample of the normal logs has been added into the log files, for the full log you will need to run the simulation yourself.

- The NB model took 9m and 39s to run the simulation.

```txt
Test set accuracy: 0.81
Confusion Matrix:
 [[69588  9412]
 [10519 16201]]
Classification Report:
               precision    recall  f1-score   support

         Ham       0.87      0.88      0.87     79000
        Spam       0.63      0.61      0.62     26720

    accuracy                           0.81    105720
   macro avg       0.75      0.74      0.75    105720
weighted avg       0.81      0.81      0.81    105720
```

## Random Forest Model Simulation

The Random Forest Model is run within the simulated network with the model results saved to the folder [RF Models](../simulation/results/RF). The logs are saved in the [Simulation Logs](../simulation/logs/RF) folder. With the results visualised in the simulation. A sample of the normal logs has been added into the log files, for the full log you will need to run the simulation yourself.

- The RF model took 20m and 55s to run the simulation.

```txt
Test set accuracy: 0.85
Confusion Matrix:
 [[78954    46]
 [15855 10865]]
Classification Report:
               precision    recall  f1-score   support

         Ham       0.83      1.00      0.91     79000
        Spam       1.00      0.41      0.58     26720

    accuracy                           0.85    105720
   macro avg       0.91      0.70      0.74    105720
weighted avg       0.87      0.85      0.82    105720
```

## Support Vector Machine Model Simulation

The Support Vector Machine Model is run within the simulated network with the model results saved to the folder [SVM Models](../simulation/results/SVM). The logs are saved in the [Simulation Logs](../simulation/logs/SVM) folder. With the results visualised in the simulation. A sample of the normal logs has been added into the log files, for the full log you will need to run the simulation yourself.

- The SVM model took 25m and 53s to run the simulation.

```txt
Test set accuracy: 0.82
Confusion Matrix:
 [[78672   328]
 [18515  8205]]
Classification Report:
               precision    recall  f1-score   support

         Ham       0.81      1.00      0.89     79000
        Spam       0.96      0.31      0.47     26720

    accuracy                           0.82    105720
   macro avg       0.89      0.65      0.68    105720
weighted avg       0.85      0.82      0.78    105720
```
