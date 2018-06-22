# Analysio
OuluHealth Hack 2018 / Hospital App Hack with OYS and Intersystems
* Analysio is a platform to enable hospitals process and analyze Hospital Information System(HIS) data. Advent of rapidly increasing medical data in healthcare domain signifies the era of Big Data and Cluster Computing. Wealth of knowledge can be obtained from from highly interdisciplinary nature of medical data. If exploited timely and appropriately, can bring enormous benefits in the form of cost savings, improved healthcare quality, and better productivity. Using Container Orchestration with Big Data analytics we can produce prediction and analytics for patients and hospital which can interoperate with current Hospital System through HL7 FHIR APIs.

## Problem
__Capturing the unprecedented medical Big Data.__

## Solution
__Providing prediction and analysis for patients and hospitals using Big Data analytics and container orchestration.__
* Docker Swarm(cluster management integrated with Docker Engine) running on hospital’s computers, providing the base for cluster computing.
  * No need to setup up separate servers for computation
  * Decentralized Design
  * Scalability and Elasticity
* Using _FHIR_ web-semantic RESTful API for exchanging medical health records and maintaining interoperation with current Hospital System.
  * Provides modern web-based suite of APIs.
  * Interoperation with legacy healthcare system and easy integration with existing system.
* Display patient by patient analysis(_on request_) as well as general hospital analysis on a web based Interface.
  * Spark’s DataFrame visualization through Plotly.
  * Analytics and plots will be displayed on Hospital/User dashboard_(built with VueJS/MaterializeCSS and NodeJS)_.

## Architecture Diagram
![architecture diagram](https://raw.githubusercontent.com/rishabhc32/Analysio/master/images/3.png)

### Use Case
#### For Patients
* Integrated view of patient data.
* Analytics of past reports, on demand health report.
* __Example__
  * __Diabetes__ - Analysis of past records, vaccination records and risk prediction(_using SVR and SVM_). 

#### For Hospital
 * __Access to knowledge resource__ - Analysis of diseases and their trends in a hospital can be useful in medical research.
 * __Clinical Decision Support(CDS)__ - Provides clinicians, staff or other individuals with knowledge and person-specific information.
 * __Example__
   * __Diabetes__ - Analysis of _How many diabetic cases, rate of survival, clustering them into large cohort(using fuzzy K-Means)_. 

### Execution during Hackathon
Demonstration of Docker Swarm cluster running on 2 or 3 laptops. Data is fetched via API calls, analyzed with scikit-learn which is distributed over the cluster, then the results are plotted using Plotly and displayed on a Web dashboard.

### Technology Stack
* Materialize/Vue(_frontend_), NodeJS(_backend_)
* FHIR API to fetch and store data
* Docker Swarm for Cluster Computing/Container Orchestration
* PySpark for data analysis - Apache Spark MLlib, GraphX
* Python
  * Scikit-learn, NumPy for prediction and clustering
  * Plotly for plotting and data visualization

### Improvements
* Extending the platform to cater more diseases rather than just cancer, diabetes, etc. thus generalizing it. 
* Making deployment process easier so that it can be deployed without knowing platform’s infrastructure details.

### Presentation Link 
* [Link](https://docs.google.com/presentation/d/1a-4DaWi7JO__eMGBYmP-3m4cmS2OvEXZz_UYzVgPBNY/edit?usp=sharing)

### Screenshots
![Web interface](https://raw.githubusercontent.com/rishabhc32/Analysio/master/images/1.PNG)

![Mobile View](https://raw.githubusercontent.com/rishabhc32/Analysio/master/images/2.PNG)
