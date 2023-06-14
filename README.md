# Beneficiary App

The Beneficiary App is a Django-based application that manages beneficiary information and assistance projects.

## Features

- Create, view, update, and delete beneficiary records.
- Manage assistance projects and enroll beneficiaries.
- Track cash assistance offered to beneficiaries.
- Generate reports and export data in CSV format.

## Installation

1. Clone the repository: master branch

   ```shell
   git clone https://github.com/scsawe/Cash_transfer-Repo.git

2. Navigate to the project directory:
cd beneficiary-app

3. Create a virtual environment:
python3 -m venv venv

4. Activate the virtual environment:

For Linux/Mac:
source venv/bin/activate
For Windows:
venv\Scripts\activate

5. Install the dependencies:
pip install -r requirements.txt

6. Run database migrations:
python manage.py migrate

7. Start the development server:
python manage.py runserver

8. Access the application in your web browser at http://localhost:8000/.

Usage
- Create an administrator account by running the following command:
python manage.py createsuperuser

- Log in to the admin interface at http://localhost:8000/admin/ to manage beneficiaries, assistance projects, and generate reports.

Contributing
Contributions are welcome! If you encounter any issues or have suggestions for improvements, please submit a pull request or open an issue in the GitHub repository.

License
MIT License

Feel free to modify the content to suit your specific beneficiary app. You can add more sections, such as "Configuration," "Testing," or "Deployment," depending on your project's requirements. Additionally, remember to include the appropriate license information in the `LICENSE` file or replace it with the license you want to use for your project.

Place this README.md file in the root directory of your beneficiary app repository, and it will serve as a helpful guide for users and contributors to understand your app and get started with it.
