import pytest
import os

# Load absolute paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "attrition_model.pkl")
SCALER_PATH = os.path.join(BASE_DIR, "models", "scaler.pkl")

def test_model_files_exist():
    assert os.path.exists(MODEL_PATH), "Model file not found"
    assert os.path.exists(SCALER_PATH), "Scaler file not found"
