# Udyam Verifier

FastAPI service to verify a Udyam registration number and company name using Playwright automation and CAPTCHA solving.

## API

**POST** `/verify`

```json
{
  "udyam_no": "UDYAM-XX-00-0000000",
  "company_name": "COMPANY NAME"
}
```

**Response:**
```json
{
  "status": "valid",
  "udyam_no": "UDYAM-XX-00-0000000",
  "company_name": "COMPANY NAME"
}
```

## Run locally

```bash
pip install -r requirements.txt
playwright install chromium
uvicorn main:app --reload
```

## Deploy on Render

Use the included `Dockerfile`. Set runtime to **Docker**.
