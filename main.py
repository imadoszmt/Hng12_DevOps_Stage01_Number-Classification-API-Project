from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
import requests
from typing import List, Dict, Union
import math

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add a root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to Number Classification API"}

def is_armstrong(n: int) -> bool:
    """Check if a number is an Armstrong number."""
    if n < 0:
        return False
    str_n = str(n)
    power = len(str_n)
    return sum(int(digit) ** power for digit in str_n) == n

def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n: int) -> bool:
    """Check if a number is perfect."""
    if n < 1:
        return False
    sum_factors = sum(i for i in range(1, n) if n % i == 0)
    return sum_factors == n

def get_properties(n: int) -> List[str]:
    """Get the properties of a number (armstrong, odd/even)."""
    properties = ["odd" if n % 2 else "even"]
    if is_armstrong(n):
        properties.insert(0, "armstrong")
    return properties

def get_digit_sum(n: int) -> int:
    """Calculate the sum of digits."""
    return sum(int(digit) for digit in str(abs(n)))

def get_fun_fact(n: int) -> str:
    """Get a fun fact about the number from the Numbers API."""
    try:
        response = requests.get(f"http://numbersapi.com/{n}/math?json")
        if response.status_code == 200:
            return response.json().get("text", f"{n} is an interesting number.")
        return f"{n} is an interesting number."
    except:
        return f"{n} is an interesting number."

@app.get("/api/classify-number")
async def classify_number(number: str, response: Response):
    """
    Classify a number and return its properties.
    """
    try:
        num = int(number)
    except ValueError:
        response.status_code = 400  
        return {  
            "number": number,  
            "error": True
        }
    
    return {
        "number": num,
        "is_prime": is_prime(num),
        "is_perfect": is_perfect(num),
        "properties": get_properties(num),
        "digit_sum": get_digit_sum(num),
        "fun_fact": get_fun_fact(num)
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
