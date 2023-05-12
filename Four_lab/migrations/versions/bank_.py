"""empty message

Revision ID: bank
Revises: b1a6b78425ed
Create Date: 2023-05-11 10:47:19.814611

"""
from alembic import op
from sqlalchemy import orm

from src.models import User, Account, Deposit

# revision identifiers, used by Alembic.
revision = 'bank'
down_revision = 'b3e92f2ae155'
branch_labels = None
depends_on = None


def upgrade() -> None:
    bind = op.get_bind()
    session = orm.Session(bind=bind)

    ivanov = User(user_name = "Ivanov Ivan Ivanovich", passport = "1234567890", address = "street, 7", phone = "88005553535", email = "ivanova@mail.ru", hashed_password = "qwe123")
    petrov = User(user_name = "Petrov Petr Petrovich", passport = "1234567890", address = "street, 7", phone = "88005553535", email = "petrova@mail.ru", hashed_password = "asd123")

    session.add_all([ivanov, petrov])
    session.flush()

    victory = Deposit(deposit_name = "Pobeda", shelf_life = 13, bet = 7)
    
    session.add_all([victory])
    session.flush()


    #account_victory_i = Account(owner_acc_id = ivanov.id, owner_dep_id = victory.id, date_open = "", date_close = "", amount = 10000)
    #account_victory_p = Account(owner_acc_id = petrov.id, owner_dep_id = victory.id, date_open = "", date_close = "", amount = 15000)
    account_victory_i = Account(owner_acc_id = ivanov.id, owner_dep_id = victory.id, amount = 10000)
    account_victory_p = Account(owner_acc_id = petrov.id, owner_dep_id = victory.id, amount = 15000)

    session.add_all([account_victory_i, account_victory_p])
    session.commit()



def downgrade() -> None:
    pass
