import typer

app = typer.Typer()
model_app = typer.Typer()  # Changed from models_app
app.add_typer(model_app, name="model")  # Changed from models

handler_app = typer.Typer()  # Renamed from users_app
app.add_typer(handler_app, name="handler")  # Renamed from users

migrate_app = typer.Typer()  # Renamed from users_app
app.add_typer(migrate_app, name="migrate")  # Renamed from users

db_app = typer.Typer()  # New sub-Typer for "db"
app.add_typer(db_app, name="db")

@model_app.command("create")  # Changed from models_create
def model_create(model: str):  # Changed from item
    print(f"Creating model: {model}")

@model_app.command("delete")  # Changed from models_delete
def model_delete(model: str):  # Changed from item
    print(f"Deleting model: {model}")

@model_app.command("sell")  # Changed from models_sell
def model_sell(model: str):  # Changed from item
    print(f"Selling model: {model}")

@handler_app.command("create")  # Renamed from users_create
def handler_create(user_name: str):  # Renamed from users_create
    print(f"Creating user: {user_name}")

@handler_app.command("delete")  # Renamed from users_delete
def handler_delete(user_name: str):  # Renamed from users_delete
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

@db_app.command("init")  # Added "init" command for "db"
def db_init():
    print("Initializing the database")

@db_app.command("seed")  # Added "seed" command for "db"
def db_seed():
    print("Seeding the database")

@db_app.command("wipe")  # Added "wipe" command for "db"
def db_wipe():
    print("Wiping the database")

if __name__ == "__main__":
    app()
