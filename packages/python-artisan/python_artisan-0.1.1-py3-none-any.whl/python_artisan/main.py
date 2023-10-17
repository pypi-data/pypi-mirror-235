import os
import re

import typer

app = typer.Typer()
model_app = typer.Typer()
app.add_typer(model_app, name="model")

handler_app = typer.Typer()
app.add_typer(handler_app, name="handler")

migrate_app = typer.Typer()
app.add_typer(migrate_app, name="migrate")

request_app = typer.Typer()
app.add_typer(request_app, name="request")

seed_app = typer.Typer()
app.add_typer(seed_app, name="seed")

db_app = typer.Typer()
app.add_typer(db_app, name="db")


@model_app.command("create")
def model_create(name: str):
    home_directory = os.path.dirname(os.path.abspath(__file__))
    result = os.path.join(home_directory, "stubs", "model")

    source_file_name = "default.stub"  # Replace with your actual file name
    source_file_name = os.path.join(result, source_file_name)

    current_directory = os.getcwd()
    source_file_path = source_file_name

    user_input_filename = name + ".py"
    destination_filename = re.sub(r"\d", "", user_input_filename).lower()
    destination_folder = "models"
    destination_file_path = os.path.join(
        current_directory, destination_folder, destination_filename
    )

    try:
        # Check if the 'handlers' folder exists, and create it if it doesn't
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
            print(f"Created '{destination_folder}' folder.")

        # Check if the destination file already exists
        if not os.path.exists(destination_file_path):
            # Read the content from the source file
            with open(source_file_path, "r") as source_file:
                handler_stub_content = source_file.read()

            # Write the content to the destination file
            with open(destination_file_path, "w") as destination_file:
                destination_file.write(handler_stub_content)

            print(f"File '{destination_file_path}' created successfully.")
        else:
            print(f"File '{destination_file_path}' already exists. Skipping creation.")

    except FileNotFoundError:
        print(f"File '{source_file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


@model_app.command("delete")
def model_delete(file_name: str):
    folder_path = "models"
    file_name = file_name + ".py"
    file_name = os.path.join(folder_path, file_name)
    file_path = os.path.join(os.getcwd(), file_name)

    if os.path.exists(file_path):
        os.remove(file_path)
        print(
            f'File "{file_path}" in the current working directory deleted successfully.'
        )
    else:
        print(
            f'File "{file_path}" in the current working directory does not exist. No deletion needed.'
        )


@handler_app.command("create")
def handler_create(
    name: str,
    subscribe: str = typer.Option(None, "--subscribe", help="Subscribe option"),
):
    home_directory = os.path.dirname(os.path.abspath(__file__))

    result = os.path.join(home_directory, "stubs", "handler")

    if subscribe is not None:
        if subscribe == "sqs":
            source_file_name = "sqs.stub"  # Replace with your actual file name
            source_file_name = os.path.join(result, source_file_name)
        else:
            source_file_name = "sns.stub"  # Replace with your actual file name
            source_file_name = os.path.join(result, source_file_name)
    else:
        source_file_name = "default.stub"  # Replace with your actual file name
        source_file_name = os.path.join(result, source_file_name)
        print("Not subscribed.")

    current_directory = os.getcwd()
    source_file_path = source_file_name

    user_input_filename = name + ".py"
    destination_filename = re.sub(r"\d", "", user_input_filename).lower()
    destination_folder = "handlers"
    destination_file_path = os.path.join(
        current_directory, destination_folder, destination_filename
    )

    try:
        # Check if the 'handlers' folder exists, and create it if it doesn't
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
            print(f"Created '{destination_folder}' folder.")

        # Check if the destination file already exists
        if not os.path.exists(destination_file_path):
            # Read the content from the source file
            with open(source_file_path, "r") as source_file:
                handler_stub_content = source_file.read()

            # Write the content to the destination file
            with open(destination_file_path, "w") as destination_file:
                destination_file.write(handler_stub_content)

            print(f"File '{destination_file_path}' created successfully.")
        else:
            print(f"File '{destination_file_path}' already exists. Skipping creation.")

    except FileNotFoundError:
        print(f"File '{source_file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


@handler_app.command("delete")
def handler_delete(file_name: str):
    folder_path = "handlers"
    file_name = file_name + ".py"
    file_name = os.path.join(folder_path, file_name)
    file_path = os.path.join(os.getcwd(), file_name)

    if os.path.exists(file_path):
        os.remove(file_path)
        print(
            f'File "{file_path}" in the current working directory deleted successfully.'
        )
    else:
        print(
            f'File "{file_path}" in the current working directory does not exist. No deletion needed.'
        )


@request_app.command("create")
def request(name: str):
    home_directory = os.path.dirname(os.path.abspath(__file__))
    result = os.path.join(home_directory, "stubs", "request")

    source_file_name = "default.stub"  # Replace with your actual file name
    source_file_name = os.path.join(result, source_file_name)

    current_directory = os.getcwd()
    source_file_path = source_file_name

    user_input_filename = name + ".py"
    destination_filename = re.sub(r"\d", "", user_input_filename).lower()
    destination_folder = "requests"
    destination_file_path = os.path.join(
        current_directory, destination_folder, destination_filename
    )

    try:
        # Check if the 'handlers' folder exists, and create it if it doesn't
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
            print(f"Created '{destination_folder}' folder.")

        # Check if the destination file already exists
        if not os.path.exists(destination_file_path):
            # Read the content from the source file
            with open(source_file_path, "r") as source_file:
                handler_stub_content = source_file.read()

            # Write the content to the destination file
            with open(destination_file_path, "w") as destination_file:
                destination_file.write(handler_stub_content)

            print(f"File '{destination_file_path}' created successfully.")
        else:
            print(f"File '{destination_file_path}' already exists. Skipping creation.")

    except FileNotFoundError:
        print(f"File '{source_file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


@request_app.command("delete")
def handler_delete(file_name: str):
    folder_path = "requests"
    file_name = file_name + ".py"
    file_name = os.path.join(folder_path, file_name)
    file_path = os.path.join(os.getcwd(), file_name)

    if os.path.exists(file_path):
        os.remove(file_path)
        print(
            f'File "{file_path}" in the current working directory deleted successfully.'
        )
    else:
        print(
            f'File "{file_path}" in the current working directory does not exist. No deletion needed.'
        )


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
