import pandas as pd
from pathlib import Path
from google import genai
import time
keys=['AIzaSyABEGShLUn0cHH9ZTy7OdLmGQVmIFVsDX8','AIzaSyAzvUcwbJfi90kLAeRVPbybqekcw9_QrHI','AIzaSyAcD1SFmVkmfefm7PXUw2WKVaEAqAMhHOs']
# Initialize the Gemini client
client = genai.Client(api_key="AIzaSyABEGShLUn0cHH9ZTy7OdLmGQVmIFVsDX8")
