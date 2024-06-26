from lighting.your_app.users import db, create_app
from your_app.models import Light

app = create_app()
app.app_context().push()

def add_example_lights():
    light1 = Light(name='Modern Pendant Light', category='Pendant', image_file='pendant1.jpg')
    light2 = Light(name='Classic Chandelier', category='Chandelier', image_file='chandelier1.jpg')
    light3 = Light(name='LED Ceiling Light', category='Ceiling', image_file='ceiling1.jpg')

    db.session.add(light1)
    db.session.add(light2)
    db.session.add(light3)
    db.session.commit()
    print("Example lights added!")

if __name__ == '__main__':
    add_example_lights()
