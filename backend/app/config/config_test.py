import pytest
from datetime import datetime
from your_app import create_app
from ..extensions import db
from ..models import Order, OrderStatus, User, Payment, Book, Category, OrderItem


@pytest.fixture(scope='session')
def app():
    app = create_app(config_object={
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:',
        'SQLALCHEMY_TRACK_MODIFICATIONS': False
    })

    with app.app_context():
        yield app


@pytest.fixture(scope='session')
def _db(app):
    db.create_all()
    yield db
    db.drop_all()


@pytest.fixture(scope='function')
def session(_db):
    connection = _db.engine.connect()
    transaction = connection.begin()

    session = _db.create_scoped_session(options={
        'bind': connection,
        'binds': {}
    })

    _db.session = session

    yield session

    transaction.rollback()
    connection.close()
    session.remove()


@pytest.fixture(scope='function')
def seed_test_data(session):
    u1 = User(name="Maria Brown", email="maria@gmail.com", phone="988888888", password="123456", identifier="550.530.420.16")
    u2 = User(name="Alex Green", email="alex@gmail.com", phone="977777777", password="123456", identifier ="440.445.870.25")
    session.add_all([u1, u2])
    session.commit()

    o1 = Order(
        moment=datetime(2019, 6, 20, 19, 53, 7),
        order_status=OrderStatus.PAID.value,
        client_id=u1.id
    )

    o2 = Order(
        moment=datetime(2019, 7, 21, 3, 42, 10),
        order_status=OrderStatus.SHIPPED.value,
        client_id=u2.id
    )

    o3 = Order(
        moment=datetime(2019, 7, 22, 15, 21, 22),
        order_status=OrderStatus.WAITING_PAYMENT.value,
        client_id=u1.id
    )

    db.session.add_all([o1, o2, o3])
    db.session.commit()

    cat1 = Category(name="Romance")
    cat2 = Category(name="Horror")
    cat3 = Category(name="Action")
    session.add_all([cat1, cat2, cat3])
    session.commit()

    b1 = Book(
        name="The Lord of the Rings",
        description="Lorem ipsum dolor sit amet, consectetur.",
        price=90.5,
        img_url=""
    )
    b2 = Book(
        name="Vagabond",
        description="Nulla eu imperdiet purus. Maecenas ante.",
        price=2190.0,
        img_url=""
    )
    b3 = Book(
        name="Clean code",
        description="Nam eleifend maximus tortor, at mollis.",
        price=1250.0,
        img_url=""
    )
    b4 = Book(
        name="Rezendeevil between two worlds",
        description="Donec aliquet odio ac rhoncus cursus.",
        price=1200.0,
        img_url=""
    )
    b5 = Book(
        name="Lion King",
        description="Cras fringilla convallis sem vel faucibus.",
        price=100.99,
        img_url=""
    )

    b1.categories.append(cat2)
    b2.categories.extend([cat1, cat3])
    b3.categories.append(cat3)
    b4.categories.append(cat3)
    b5.categories.append(cat2)

    session.add_all([b1, b2, b3, b4, b5])
    session.commit()

    oi1 = OrderItem(order_id=o1.id, book_id=b1.id, quantity=2, price=b1.price)
    oi2 = OrderItem(order_id=o1.id, book_id=b3.id, quantity=1, price=b3.price)
    oi3 = OrderItem(order_id=o2.id, book_id=b3.id, quantity=2, price=b3.price)
    oi4 = OrderItem(order_id=o3.id, book_id=b5.id, quantity=2, price=b5.price)
    session.add_all([oi1, oi2, oi3, oi4])

    pay1 = Payment(
        moment=datetime(2019, 6, 20, 21, 53, 7),
        order_id=o1.id)

    try:
        session.add(pay1)
        o1.payment = pay1  # Set the bidirectional relationship
        session.commit()
        print("Payment created and associated with order successfully!")
    except Exception as e:
        session.rollback()
        print(f"Error creating payment: {str(e)}")
        raise

    return {
        'users': [u1, u2],
        'orders': [o1, o2, o3],
        'categories': [cat1, cat2, cat3],
        'products': [b1, b2, b3, b4, b5],
        'order_items': [oi1, oi2, oi3, oi4],
        'payment': pay1
    }