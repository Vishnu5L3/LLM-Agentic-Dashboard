from fastapi import FastAPI
import subprocess
import uvicorn

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the MLflow Dashboard!"}

if __name__ == "__main__":
    # Start the MLflow server in the background
    mlflow_process = subprocess.Popen(
        ["mlflow", "ui", "--host", "0.0.0.0", "--port", "5000"]
    )

    # Start the FastAPI app
    try:
        uvicorn.run(app, host="0.0.0.0", port=8000)
    finally:
        # Ensure the MLflow server is terminated when the script exits
        mlflow_process.terminate()