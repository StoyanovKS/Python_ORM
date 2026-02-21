# Python ORM Course Workspace

This workspace contains a sequence of Django ORM and SQLAlchemy exercises. Each numbered folder represents a lesson or exercise set. Most Django folders follow a shared structure (a Django project with a single app, a skeleton directory used by the exercises, and helper scripts).

## Installation (Python 3.12)

Create and activate a virtual environment from the Python_ORM root, then install the baseline dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Some lessons have their own requirements files. If a specific folder has a requirements file, install it instead (or in addition) to match that lesson:

```powershell
pip install -r <lesson-folder>\requirements.txt
```

The SQLAlchemy lesson uses a file named requirments.txt (note the spelling) in 20.SQL_Alchemy.

## Folder guide

### 03.Introduction_to_ORM
- 0.1.sql_injection/ - A small script demo focused on SQL injection.
  - sql_injection.py - Standalone Python script for the injection example.
- 2.task/ - A starter Django project used for introductory ORM tasks.
  - caller.py - Entry point used by automated checks or local runs.
  - manage.py - Standard Django management script.
  - main_app/ - The Django app where models and queries live.
  - orm_skeleton/ - Provided skeleton and tests or task scaffolding.
  - requirements.txt - Python dependencies for this lesson.
  - .idea/ - Local IDE settings (optional).

### 04.Django_Model_Basic
- A Django project focused on basic model definitions.
- .idea/ - Local IDE settings (optional).
- app_name/ - A Django app used for early model exercises.
- caller.py, manage.py, pack.py - Helper scripts for running or packaging.
- main_app/ - Primary app with model tasks.
- orm_skeleton/ - Task scaffolding and starter code.
- db.sqlite3 - Local development database snapshot.
- requirements.txt - Python dependencies.
- submission-20-09_27.10.24.zip - Submission archive.

### 05.Django_Model_Basic
- A second set of basic model exercises with the same project layout.
- .idea/, .vscode/ - Local editor settings (optional).
- caller.py, manage.py, pack.py - Helper scripts for running or packaging.
- main_app/, orm_skeleton/ - App code and scaffolding.
- db.sqlite3 - Local development database snapshot.
- requirements.txt - Python dependencies.
- submission-21-54_27.10.24.zip - Submission archive.

### 06.Migrations_and_Django_Admin
- Migrations and admin configuration tasks.
- caller.py, manage.py, pack.py - Helper scripts for running or packaging.
- main_app/, orm_skeleton/ - App code and scaffolding.
- requirements.txt - Python dependencies.
- submission-13-12_01.11.24.zip - Submission archive.

### 07.Migrations_and_Django_Admin_Exercise
- Additional migration and admin exercises.
- .vscode/ - Local editor settings (optional).
- caller.py, manage.py, pack.py - Helper scripts for running or packaging.
- main_app/, orm_skeleton/ - App code and scaffolding.
- requirements.txt - Python dependencies.
- submission-14-50_01.11.24.zip - Submission archive.

### 08.Data_operations_in_Django_with_queries
- Basic CRUD and query operations in Django.
- caller.py, manage.py, pack.py - Helper scripts for running or packaging.
- main_app/, orm_skeleton/ - App code and scaffolding.
- requirements.txt - Python dependencies.
- submission-15-23_01.11.24.zip - Submission archive.

### 09.Data_operations_in_Django_with_queries_exercise
- More advanced data operations and query practice.
- .vscode/ - Local editor settings (optional).
- caller.py, manage.py, pack.py - Helper scripts for running or packaging.
- main_app/, orm_skeleton/ - App code and scaffolding.
- populate_db_script.py - Utility script for seeding data.
- requirements.txt - Python dependencies.
- submission-17-13_01.11.24.zip - Submission archive.
- __pycache__/ - Local Python bytecode cache.

### 10.Queries_with_Django
- Focused on query patterns and ORM filters.
- caller.py, manage.py, pack.py - Helper scripts for running or packaging.
- main_app/, orm_skeleton/ - App code and scaffolding.
- requirements.txt - Python dependencies.
- submission-21-16_06.11.24.zip - Submission archive.

### 11.Queries_with_Django_exercise
- Additional query exercises with the same Django project layout.
- caller.py, manage.py, pack.py - Helper scripts for running or packaging.
- main_app/, orm_skeleton/ - App code and scaffolding.
- requirements.txt - Python dependencies.
- submission-21-43_06.11.24.zip - Submission archive.

### 12.Django_model_relations
- One-to-one, one-to-many, and many-to-many relations.
- caller.py, manage.py, pack.py - Helper scripts for running or packaging.
- main_app/, orm_skeleton/ - App code and scaffolding.
- requirements.txt - Python dependencies.
- submission-22-10_06.11.24.zip - Submission archive.

### 13.Django_model_relations_exercise
- Relation exercises with the same project layout.
- caller.py, manage.py, pack.py - Helper scripts for running or packaging.
- main_app/, orm_skeleton/ - App code and scaffolding.
- requirements.txt - Python dependencies.
- submission-22-31_06.11.24.zip - Submission archive.

### 14.Django_models_inheritance
- Model inheritance strategies (abstract, multi-table, proxy).
- .vscode/ - Local editor settings (optional).
- caller.py, manage.py, pack.py - Helper scripts for running or packaging.
- main_app/, orm_skeleton/ - App code and scaffolding.
- requirements.txt - Python dependencies.
- submission-18-52_08.11.24.zip - Submission archive.

### 15.Django_models_inheritance_exercise
- Inheritance exercises using the same project layout.
- caller.py, manage.py, pack.py - Helper scripts for running or packaging.
- main_app/, orm_skeleton/ - App code and scaffolding.
- requirements.txt - Python dependencies.
- submission-19-11_08.11.24.zip - Submission archive.

### 16.Advanced_Django
- Advanced ORM features and patterns.
- caller.py, manage.py, pack.py - Helper scripts for running or packaging.
- main_app/, orm_skeleton/ - App code and scaffolding.
- requirements.txt - Python dependencies.
- submission-19-34_08.11.24.zip - Submission archive.

### 17.Advanced_Django_exercise
- Advanced exercises with the same project layout.
- caller.py, manage.py, pack.py - Helper scripts for running or packaging.
- main_app/, orm_skeleton/ - App code and scaffolding.
- requirements.txt - Python dependencies.
- submission-19-57_08.11.24.zip - Submission archive.
- .DS_Store - macOS metadata (optional).

### 18.Advanced_queries_Django
- Advanced query techniques and aggregations.
- caller.py, manage.py, pack.py - Helper scripts for running or packaging.
- main_app/, orm_skeleton/ - App code and scaffolding.
- db.sqlite3 - Local development database snapshot.
- requirements.txt - Python dependencies.
- submission-20-53_08.11.24.zip - Submission archive.

### 19.Advanced_queries_Django_exercise
- Exercises focused on advanced queries.
- caller.py, manage.py, pack.py - Helper scripts for running or packaging.
- main_app/, orm_skeleton/ - App code and scaffolding.
- db.sqlite3 - Local development database snapshot.
- requirements.txt - Python dependencies.
- submission-21-03_08.11.24.zip - Submission archive.

### 20.SQL_Alchemy
- SQLAlchemy lesson with Alembic migrations.
- alembic/ - Alembic versions and migration environment.
- alembic.ini - Alembic configuration.
- models.py - SQLAlchemy models.
- transactions.py - Transaction or session examples.
- main.py, main2.py - Script entry points for demos.
- requirments.txt - Dependency list (note the filename spelling).
- __pycache__/ - Local Python bytecode cache.

### 21.SQL_Alchemy_exercise
- SQLAlchemy exercises with helper scripts.
- alembic/ - Alembic versions and migration environment.
- alembic.ini - Alembic configuration.
- models.py - SQLAlchemy models.
- helpers.py - Helper utilities for the exercise.
- seed.py - Seed data loader.
- caller.py - Entry point used by checks or local runs.
- __pycache__/ - Local Python bytecode cache.

### 22.EX1
- Exercise set 1, Django project layout.
- caller.py, manage.py, pack.py - Helper scripts for running or packaging.
- main_app/, orm_skeleton/ - App code and scaffolding.
- requirements.txt - Python dependencies.
- venv/ - Local virtual environment (optional).

### 23.EX2
- Exercise set 2, Django project layout.
- caller.py, manage.py, pack.py - Helper scripts for running or packaging.
- main_app/, orm_skeleton/ - App code and scaffolding.
- requirements.txt - Python dependencies.
- venv/ - Local virtual environment (optional).

### 24.EX3
- Exercise set 3, Django project layout.
- caller.py, manage.py, pack.py - Helper scripts for running or packaging.
- main_app/, orm_skeleton/ - App code and scaffolding.
- requirements.txt - Python dependencies.


### 25.EX4
- Exercise set 4, Django project layout.
- caller.py, manage.py, pack.py - Helper scripts for running or packaging.
- main_app/, orm_skeleton/ - App code and scaffolding.
- requirements.txt - Python dependencies.

