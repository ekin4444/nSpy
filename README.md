# NeuroSpy: Brain Tumor Detection Website

NeuroSpy is a web application designed to assist in the early detection of brain tumors using Convolutional Neural Networks (CNN) and machine learning. Users can upload MRI images for analysis and receive a prediction about the presence of a brain tumor. The platform also includes educational resources, a symptom checker, and doctor recommendations to raise awareness about brain cancer.

---

## Features

- **MRI Image Analysis**: Upload MRI images and receive real-time predictions.
- **Educational Resources**: Access articles, videos, and information about brain cancer.
- **Symptom Checker**: Evaluate symptoms and get recommendations.
- **Doctor Recommendations**: Search for medical professionals based on specific filters.
- **Donation Page**: Support brain cancer research and awareness efforts.
- **Secure User Authentication**: Protect accounts and uploaded data with a robust login system.

---

## Prerequisites

To run this project, ensure you have the following installed:

1. **Python 3.8 or higher**
2. **pip** (Python package installer)
3. **Virtual Environment** module (`venv`)

---

## Installation

Follow these steps to set up the project locally:

### 1. Clone the Repository
```bash
git clone https://github.com/ekin4444/nSpy.git
cd nSpy
2. Create a Virtual Environment
bash
Copy
Edit
python -m venv .venv
3. Activate the Virtual Environment
Windows:
bash
Copy
Edit
.\.venv\Scripts\activate
Mac/Linux:
bash
Copy
Edit
source .venv/bin/activate
4. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
5. Apply Migrations
bash
Copy
Edit
python manage.py migrate
6. Run the Development Server
bash
Copy
Edit
python manage.py runserver
7. Open in Browser
Visit http://127.0.0.1:8000/ in your web browser.

Project Structure
plaintext
Copy
Edit
nSpy/
├── myapp/              # Django app with views, models, and templates
│   ├── migrations/     # Database migration files
│   ├── static/         # Static files (CSS, JavaScript, images)
│   ├── templates/      # HTML templates
│   ├── models.py       # Database models
│   ├── views.py        # Application logic
│   ├── urls.py         # URL routes
├── .venv/              # Virtual environment (not included in Git)
├── manage.py           # Django management script
├── requirements.txt    # Project dependencies
├── README.md           # Project documentation
└── LICENSE             # License information
Security and Privacy
Uploaded MRI images are processed locally and not permanently stored.
All user accounts are protected with hashed passwords and secure sessions.
Sensitive information is excluded from the repository using .gitignore.
Contributing
We welcome contributions to improve NeuroSpy. Here's how you can contribute:

Fork the repository.
Create a feature branch:
bash
Copy
Edit
git checkout -b feature-name
Commit your changes:
bash
Copy
Edit
git commit -m "Description of changes"
Push to your branch:
bash
Copy
Edit
git push origin feature-name
Open a pull request on GitHub.
License
This project is licensed under the MIT License. You are free to use, modify, and distribute the code with proper attribution.

Acknowledgments
Machine Learning: TensorFlow and Keras for the CNN model.
Frontend: Bootstrap for responsive design.
Backend: Django for managing application logic and database operations.
