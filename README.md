# Predictive Healthcare Analytics for Insurance

An AI-driven health risk assessment system for insurance personalization, analyzing medical history, lifestyle factors, and demographic data to predict insurance risk scores and suggest tailored policies.

## Features

- AI-based risk assessment for insurance applicants
- Personalized policy recommendations
- Integration with real-world insurance datasets and APIs
- Secure cloud-based deployment
- Interactive dashboard for users and insurers
- HIPAA-compliant data handling

## Tech Stack

- **Backend:** FastAPI (Python)
- **Frontend:** React.js, Tailwind CSS
- **Database:** PostgreSQL
- **ML:** Scikit-learn, TensorFlow
- **Cloud:** AWS SageMaker

## Project Structure

```
healthcare-analytics/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── models/
│   │   ├── schemas/
│   │   └── services/
│   ├── tests/
│   └── main.py
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   └── utils/
│   └── public/
├── ml/
│   ├── models/
│   ├── data/
│   └── training/
└── docs/
```

## Setup Instructions

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```
5. Run the development server:
   ```bash
   uvicorn backend.main:app --reload
   ```

## API Documentation

Once the server is running, visit:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Security

- All data is encrypted at rest and in transit
- HIPAA compliance measures implemented
- JWT-based authentication
- Role-based access control

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 