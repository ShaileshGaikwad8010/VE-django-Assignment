# VE-django-Assignment


#CSV Analyzer
CSV Analyzer is a Django web application for uploading, analyzing, and visualizing CSV data.

*Features
 -Upload CSV files for analysis.
 -Generate visualizations such as histograms and line charts.
 -Store and manage uploaded files.
 
*Setup Instructions
 -Prerequisites
 -Python 3.8+
 -Django 3.2+
 -SQLite (for development and testing purposes)


 *Installation:

 1.Clone the repository:
 		git clone <repository_url>
		cd csv_analyzer

 2.Create and activate a virtual environment:
 		python -m venv venv
		source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3.Install dependencies:
		pip install -r requirements.txt

4.Apply database migrations:
		python manage.py migrate

5.Run the development server:
		python manage.py runserver





*Project Structure:

csv_analyzer/: Main project directory.
		-manage.py: Django's command-line utility.
			-db.sqlite3: SQLite database file.
			-csv_analyzer/: Django project settings.
			-analysis/: Django app for CSV analysis.
						-templates/analysis/: HTML templates.
						-migrations/: Database migrations.
						-media/: Uploaded files and generated images.
						-models.py: Database models.
						-views.py: Application views.
						-urls.py: URL configurations.
						-forms.py: Forms for file upload.

	 
*Usage:

Upload CSV files:
		-Navigate to the upload page and select a CSV file to upload.

Analyze data:
		-After uploading, view various visualizations and analysis results generated from the data.

