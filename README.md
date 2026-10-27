Markdown
# Assignment Submission Portal - DevOps Lab Midterm

## Overview
A simple assignment submission portal with an automated CI/CD testing pipeline and local test report receiver.

## Requirements Implemented
1. **Assignment Portal:** Built using Python/Flask to accept student details and submission URLs.
2. **Automated Tests:** Implemented using Pytest covering valid submissions, missing registration numbers, and invalid URLs.
3. **CI/CD Pipeline:** Configured with GitHub Actions to run tests on every push.
4. **Local HTTP Receiver:** Receives test reports from GitHub Actions and saves them locally as `test-report.json`.

## How to Run Locally
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
Start the local receiver:

Bash
python receiver.py
Run tests:

Bash
python -m pytest
