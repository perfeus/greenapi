# Green API WhatsApp Integration

Flask web application for WhatsApp messaging integration using Green API. Send messages and files through WhatsApp programmatically.

## Features
- 📱 Send text messages to WhatsApp numbers
- 📁 Send files via URL to WhatsApp contacts
- ⚙️ Get account settings
- 📊 Check instance state
- 🎨 Bootstrap-based UI interface

## Tech Stack
- Python 3.10.16
- Flask
- Green API
- Bootstrap 4.6
- Requests library

## Quick Start
```bash
git clone https://github.com/yourusername/green-api.git
cd green-api
```

## Create virtual environment
```bash
python3.10 -m venv venv
source venv/bin/activate
```

## Install dependencies
```bash
pip install -r requirements.txt
```

## Run application
```bash
python main.py
```

## Project Structure
green_api/
├── main.py           # Main Flask application
├── static/           # Static files (CSS, JS)
├── templates/        # HTML templates
├── requirements.txt  # Python dependencies
└── Procfile          # Heroku deployment
└── README.md         # Documentation

## API Endpoints
- POST /sendMessage - Send WhatsApp message
- POST /sendFileByUrl - Send file via URL
- GET /getSettings - Get account settings
- GET /getStateInstance - Check instance state

## Contributing
1. Fork repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Open pull request

## License
MIT License

Author
Aleksei Izmalkin