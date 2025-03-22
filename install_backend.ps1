# Create and activate virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Create .env file from example
Copy-Item .env.example .env

Write-Host "Backend dependencies installed successfully!"
Write-Host "Please update the .env file with your configuration." 