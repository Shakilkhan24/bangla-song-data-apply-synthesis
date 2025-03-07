import pandas as pd
from pathlib import Path
from google import genai
import time

# Initialize the Gemini client
client = genai.Client(api_key="AIzaSyBJuESqnScwhxn5A8g6viyLpKhp_V-hF7E")
