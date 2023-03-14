# Django App: Save GitHub JSON to SQL Database

This Django app allows you to clone a GitHub repository and save its JSON data to an SQL database Asynchronously using celery.

ScreenShots:

![gitsync1](https://user-images.githubusercontent.com/32688387/225042349-a17778ad-e7a7-4076-91f1-8670965c00f5.png)
![gitsync-1](https://user-images.githubusercontent.com/32688387/225042410-25a0c307-bdb1-495d-a2c5-081ba2aa6f7b.png)
![gitsync2](https://user-images.githubusercontent.com/32688387/225042537-9a6e89b6-5afa-411b-9143-abddf90deaab.png)
![gitsync3](https://user-images.githubusercontent.com/32688387/225042553-a88ad31f-1fe3-4c3c-bead-307ecb189f2e.png)
![gitsync4](https://user-images.githubusercontent.com/32688387/225042554-14ece648-adc8-4d3e-ae7f-1ebb4fe94f06.png)


## Requirements

To use this app, you will need:

- Python 3.x
- Django 3.x
- Git
- An SQL database (e.g. PostgreSQL)

## Installation

1. Clone the repository:

`git clone https://github.com/your_username/gitsynchub.git`


2. Install the required packages:

`pip install -r requirements.txt`

3. Run the migrations:

`python manage.py migrate`

4. Start the development server:

`python manage.py runserver`

5. Access the app in your web browser at `http://localhost:8000/.`

## Usage

1. Enter the GitHub repository URL in the input field.
2. Click the "Clone and Save" button.
3. Wait for the app to clone the repository and save its JSON data to the SQL database.
4. Check the SQL database to ensure that the JSON data was saved correctly.

## Example

To clone the repository at https://github.com/octocat/hello-world and save its JSON data to an SQL database, enter the following URL in the input field:

`https://github.com/octocat/hello-world.git`

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## License

This app is licensed under the MIT License.

---
