# Phishing Email Detector

A simple web application that detects suspicious phrases and links in email text to help identify potential phishing attempts. Built with Python Flask for the backend and plain HTML/JavaScript for the frontend.

## Features

- Paste raw email text into a textarea.
- Detects common phishing phrases such as:
  - "verify your account"
  - "urgent"
  - "click here"
  - "login"
  - "password"
- Extracts suspicious links starting with "http".
- Displays the results on the page instantly.

## Tech Stack

- Backend: Python, Flask, Flask-CORS
- Frontend: HTML, JavaScript (Fetch API)

## Getting Started

### Prerequisites

- Python 3.x installed
- `pip` package manager

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/KP3530/phishing-email-detector.git
   cd phishing-email-detector
