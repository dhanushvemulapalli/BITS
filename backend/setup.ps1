# Create virtual environment
python -m venv venv

# Activate virtual environment
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Create .env file from example
Copy-Item .env.example .env

Write-Host "Backend setup complete! Please update the .env file with your database credentials."
Write-Host "To start the server, run: uvicorn main:app --reload" 