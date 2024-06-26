from your_app import create_app
from your_app.initial_data import add_initial_data
from flask.cli import AppGroup

app = create_app()

# Create a custom CLI command
cli = AppGroup('custom')

@cli.command('add-initial-data')
def add_initial_data_command():
    """Add initial data to the database."""
    with app.app_context():
        add_initial_data()

# Register the custom CLI command
app.cli.add_command(cli)

if __name__ == "__main__":
    app.run(debug=True)
