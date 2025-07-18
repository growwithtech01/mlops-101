# MLOps Demo Project

This project demonstrates a simple end-to-end MLOps workflow using Docker and Kubernetes. It includes a machine learning model that is trained on a dataset and can make predictions based on new input data.

## Project Structure

```
mlops-demo
├── data
│   └── dataset.csv          # Dataset used for training and testing
├── src
│   ├── train.py             # Script to train the machine learning model
│   ├── predict.py           # Script to make predictions using the trained model
│   └── Dockerfile           # Dockerfile to build the application image
├── kubernetes
│   ├── deployment.yaml      # Kubernetes deployment configuration
│   ├── service.yaml         # Kubernetes service configuration
│   └── configmap.yaml       # ConfigMap for application configuration
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
└── .gitignore               # Files to ignore in Git
```

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd mlops-demo
   ```

2. **Install Dependencies**
   Make sure you have Python and pip installed. Then, install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Prepare the Dataset**
   Place your dataset in the `data` directory as `dataset.csv`. Ensure it contains the necessary features and labels.

4. **Train the Model**
   Run the training script to train the model and save it:
   ```bash
   python src/train.py
   ```

5. **Build the Docker Image**
   Navigate to the `src` directory and build the Docker image:
   ```bash
   cd src
   docker build -t mlops-demo .
   ```

6. **Deploy to Kubernetes**
   Ensure Minikube is running, then apply the Kubernetes configurations:
   ```bash
   kubectl apply -f ../kubernetes/deployment.yaml
   kubectl apply -f ../kubernetes/service.yaml
   ```

7. **Access the Application**
   Use the following command to access the service:
   ```bash
   minikube service <service-name> --url
   ```

## Usage Example

After deploying the application, you can make predictions by sending requests to the exposed service endpoint. Ensure to format your input data as required by the model.

## Conclusion

This project serves as a foundational example of implementing MLOps practices using Docker and Kubernetes. You can expand upon this by adding more features, improving the model, or integrating CI/CD pipelines.