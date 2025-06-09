from flask.cli import with_appcontext
import click
import datetime

from src.ext import db
from src.models import Person, Product, IDCard, Actor, Movie, ActorMovie, University, Student, User


@click.command("init_db")
@with_appcontext
def init_db():
    click.echo("initializing database...")

    db.drop_all()
    db.create_all()

    click.echo("Initialized database")


@click.command("populate_db")
@with_appcontext
def populate_db():
    products = [
        {"id": 0, "name": "ფრანით მორბენალი", "author": "ხალიდ ჰოსეინი", "price": "25", "img": "franit-morbenali.png"},
        {"id": 1, "name": "48 კანონი", "author": "რობერტ გრინი", "price": "40", "img": "dzalauflebis_48_kanoni.jpg"},
        {"id": 2, "name": "ატომური ჩვევები", "author": "ჯეიმს ქლიერი", "price": "35", "img": "atomuri_cvevebi.jpg"},
        {"id": 3, "name": "ხაფანგი 22", "author": "ჟოზეფ ჰელერის", "price": "30", "img": "xafangi22.png"}
    ]

    for product in products:
        new_product = Product(name=product["name"], author=product["author"], price=product["price"],
                              image=product["img"])
        db.session.add(new_product)
    db.session.commit()

    ### ONE TO ONE EXAMPLE DATA ###
    id_card = IDCard(personal_number="12345678901", serial_number="XXX", expiry_date=datetime.datetime.now())
    db.session.add(id_card)
    db.session.commit()

    person = Person(name="John", surname="Doe", birthday=datetime.datetime.now(), idcard_id=id_card.id)
    db.session.add(person)
    db.session.commit()

    ### ONE TO MANY EXAMPLE DATA ###
    university = University(name="GTU", address="Teqnikuri")
    db.session.add(university)
    db.session.commit()

    student1 = Student(name="Jeiran Doadze", university_id=university.id)
    student2 = Student(name="Joanna Smth", university_id=university.id)
    db.session.add_all([student1, student2])
    db.session.commit()


    ### MANY TO MANY EXAMPLE DATA ###
    actor1 = Actor(name="Robert Downey Jr")
    actor2 = Actor(name="Chris Evans")

    movie1 = Movie(name="Iron Man", genre="Fantasy, Action")
    movie2 = Movie(name="Captain America", genre="Action")
    movie3 = Movie(name="Avengers", genre="Action")

    db.session.add_all([actor1, actor2])
    db.session.add_all([movie1, movie2, movie3])
    db.session.commit()

    actormovie1 = ActorMovie(actor_id=1, movie_id=1)
    actormovie2 = ActorMovie(actor_id=2, movie_id=2)
    actormovie3 = ActorMovie(actor_id=1, movie_id=3)
    actormovie4 = ActorMovie(actor_id=2, movie_id=3)
    db.session.add_all([actormovie1, actormovie2, actormovie3, actormovie4])
    db.session.commit()


    ### ADMIN USER ###
    User(username="admin", password="password123", profile_image="static/assets/admin.jpg", role="Admin").create()