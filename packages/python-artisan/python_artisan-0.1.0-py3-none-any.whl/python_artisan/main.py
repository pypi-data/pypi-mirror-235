import sys
import re
sys.path.append('.')
import typer
import os

app = typer.Typer()
model_app = typer.Typer()
app.add_typer(model_app, name="model")

handler_app = typer.Typer()
app.add_typer(handler_app, name="handler")

migrate_app = typer.Typer()
app.add_typer(migrate_app, name="migrate")

db_app = typer.Typer()
app.add_typer(db_app, name="db")

@model_app.command("create")
def model_create(model: str):
    print(f"Creating model: {model}")

@model_app.command("delete")
def model_delete(model: str):
    print(f"Deleting model: {model}")

@model_app.command("sell")
def model_sell(model: str):
    print(f"Selling model: {model}")

@handler_app.command("create")
def handler_create(name: str):
    # Get the current working directory
    current_directory = os.getcwd()

    # Define the source file path
    source_file_name = "lambda_stub.py"  # Replace with your actual file name
    source_file_path = os.path.join(current_directory, source_file_name)

    # Remove numbers from the user's input and convert to lowercase
    destination_filename = re.sub(r'\d', '', name).lower()

    # Define the destination folder
    destination_folder = "handlers"
    destination_file_path = os.path.join(current_directory, destination_folder, destination_filename) + ".py"

    try:
        # Check if the 'handlers' folder exists, and create it if it doesn't
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
            print(f"Created '{destination_folder}' folder.")

        # Check if the destination file already exists
        if not os.path.exists(destination_file_path):
            # Read the content from the source file
            with open(source_file_path, "r") as source_file:
                lambda_stub_content = source_file.read()

            # Write the content to the destination file
            with open(destination_file_path, "w") as destination_file:
                destination_file.write(lambda_stub_content)

            print(f"File '{destination_file_path}' created successfully.")
        else:
            print(f"File '{destination_file_path}' already exists. Skipping creation.")

    except FileNotFoundError:
        print(f"File '{source_file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")




@handler_app.command("delete")
def handler_delete(user_name: str):
    print(f"Deleting user: {user_name}")

@app.command("request")
def request(model: str, user: str):
    print(f"Requesting model: {model} for user: {user}")

@migrate_app.command("install")
def migrate():
    print("Running migration")

@migrate_app.command("drop")
def migrate_drop():
    print("Dropping migration data")

@db_app.command("init")
def db_init():
    print("Initializing the database")

@db_app.command("seed")
def db_seed():
    print("Seeding the database")

@db_app.command("wipe")
def db_wipe():
    print("Wiping the database")

if __name__ == "__main__":
    app()
