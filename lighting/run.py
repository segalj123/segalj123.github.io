from your_app import create_app

app = create_app()

if __name__ == "__main__":
    # Add initial data if it doesn't exist
    try:
        from your_app.add_initial_data import add_initial_data
        add_initial_data()
    except Exception as e:
        print(f"Error adding initial data: {e}")

    app.run(debug=True)
