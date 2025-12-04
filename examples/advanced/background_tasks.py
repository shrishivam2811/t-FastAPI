"""
Background Tasks Example

Learn how to use background tasks for operations that should run after returning a response.
Run with: uvicorn examples.advanced.background_tasks:app --reload
"""

from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
import time

app = FastAPI(title="Background Tasks API")


# Simulated email sending
def send_email(email: str, message: str):
    """
    Simulate sending an email (takes 3 seconds).
    In a real application, this would use an email service.
    """
    print(f"Starting to send email to {email}...")
    time.sleep(3)  # Simulate email sending delay
    print(f"Email sent to {email}: {message}")


def write_log(message: str):
    """
    Simulate writing to a log file.
    """
    print(f"Writing to log: {message}")
    with open("/tmp/fastapi_log.txt", "a") as log:
        log.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {message}\n")


def process_data(data: dict):
    """
    Simulate data processing that takes time.
    """
    print(f"Starting to process data: {data}")
    time.sleep(2)  # Simulate processing delay
    print(f"Finished processing data: {data}")


class EmailRequest(BaseModel):
    email: str
    subject: str
    body: str


class Order(BaseModel):
    order_id: int
    item: str
    quantity: int
    customer_email: str


@app.post("/send-notification/")
async def send_notification(email: str, background_tasks: BackgroundTasks):
    """
    Send a notification email in the background.
    The response is returned immediately while the email is sent in the background.
    
    Args:
        email: Email address to send notification to
        background_tasks: FastAPI background tasks handler
    """
    background_tasks.add_task(send_email, email, "This is your notification!")
    return {
        "message": "Notification will be sent in the background",
        "email": email
    }


@app.post("/send-email/")
async def send_email_endpoint(
    email_request: EmailRequest,
    background_tasks: BackgroundTasks
):
    """
    Send an email with custom subject and body in the background.
    
    Args:
        email_request: Email details
        background_tasks: FastAPI background tasks handler
    """
    message = f"Subject: {email_request.subject}\n\n{email_request.body}"
    background_tasks.add_task(send_email, email_request.email, message)
    return {
        "message": "Email will be sent in the background",
        "email": email_request.email
    }


@app.post("/orders/")
async def create_order(order: Order, background_tasks: BackgroundTasks):
    """
    Create an order and send confirmation email in the background.
    Multiple background tasks can be added.
    
    Args:
        order: Order details
        background_tasks: FastAPI background tasks handler
    """
    # Add multiple background tasks
    background_tasks.add_task(
        write_log,
        f"Order {order.order_id} created for {order.customer_email}"
    )
    background_tasks.add_task(
        send_email,
        order.customer_email,
        f"Order {order.order_id} confirmed: {order.quantity}x {order.item}"
    )
    background_tasks.add_task(process_data, order.model_dump())
    
    return {
        "message": "Order created successfully",
        "order_id": order.order_id,
        "note": "Confirmation email will be sent in the background"
    }


@app.post("/process/")
async def process_item(item_id: int, background_tasks: BackgroundTasks):
    """
    Process an item in the background.
    
    Args:
        item_id: ID of the item to process
        background_tasks: FastAPI background tasks handler
    """
    background_tasks.add_task(process_data, {"item_id": item_id})
    background_tasks.add_task(write_log, f"Processing item {item_id}")
    
    return {
        "message": f"Item {item_id} is being processed",
        "note": "Processing will continue in the background"
    }
