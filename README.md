# Number Classification API

A FastAPI-based API that provides mathematical properties and fun facts about numbers.

## Features

- Number classification (prime, perfect, armstrong)
- Digit sum calculation
- Fun facts about numbers
- CORS support
- Error handling

## Installation

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the server: `uvicorn main:app --reload`

## API Endpoint

1. Root endpoint:
   GET /
   Returns a welcome message

2. Number Classification:
   GET /api/classify-number?number={number}
   Returns properties of the given number

### Success Response (200 OK)
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number..."
}
```

## Live API

The API is deployed at: https://hng12-devops-stage01-number.onrender.com/api/classify-number?number=371

