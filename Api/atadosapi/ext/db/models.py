from sqlalchemy.exc import IntegrityError

from . import db


class Voluntary(db.Model):
    __tablename__ = "voluntary"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(50), nullable=False)
    surname = db.Column(db.Unicode(200), nullable=False)
    district = db.Column(db.Unicode(60))
    city = db.Column(db.Unicode(60))

    def to_dict(self) -> dict:
        return {col: getattr(self, col) for col in self.__table__.columns.keys()}

    @staticmethod
    def get(id: int) -> db.Model:
        return Voluntary.query.filter_by(id=id).first()

    def save(self) -> dict:
        try:
            db.session.add(self)
            db.session.commit()

        except IntegrityError as err:
            db.session.rollback()
            msg_err = list()

            for e in err.orig.args:
                if not ":" in str(e):
                    continue

                attr = str(e).split(":")[1]
                col = attr.split("'")[1]

                if "unique" in e.lower():
                    msg_err.append("%s já cadastrado" % (col.upper()))

                elif "null" in e.lower():
                    msg_err.append("O campo %s é obrigatorio" % (col.upper()))

                else:
                    msg_err.append("Erro desconhecido")

            response = {
                "success": False,
                "message": "Não foi possível atualizar o voluntario\nDetalhes do erro: %s"
                % ("\n".join(msg_err)),
            }

        else:
            response = {
                "success": True,
                "message": "Voluntario salvo com sucesso",
                "voluntary": self.to_dict(),
            }

        return response

    def delete(self) -> dict:
        try:
            db.session.delete(self)
            db.session.commit()

        except IntegrityError:
            db.session.rollback()
            response = {
                "success": False,
                "message": "Não foi possível excluir o voluntario",
            }

        else:
            response = {"success": True, "message": "Voluntario excluido com sucesso!"}

        return response

    def populate_obj(self, data: dict) -> dict:
        for key, value in data.items():
            if key in self.__table__.columns.keys():
                setattr(self, key, value)


class Actions(db.Model):
    __tablename__ = "actions"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(100), nullable=False)
    district = db.Column(db.Unicode(100), nullable=False)
    address = db.Column(db.Unicode(100), nullable=False)
    city = db.Column(db.Unicode(60), nullable=False)
    description = db.Column(db.Unicode(100), nullable=False)

    def to_dict(self) -> dict:
        return {col: getattr(self, col) for col in self.__table__.columns.keys()}

    @staticmethod
    def get(id: int) -> db.Model:
        return Actions.query.filter_by(id=id).first()

    def save(self) -> dict:
        try:
            db.session.add(self)
            db.session.commit()

        except IntegrityError as err:
            db.session.rollback()
            msg_err = list()

            for e in err.orig.args:
                if not ":" in str(e):
                    continue

                attr = str(e).split(":")[1]
                col = attr.split("'")[1]

                if "unique" in e.lower():
                    msg_err.append("%s já cadastrado" % (col.upper()))

                elif "null" in e.lower():
                    msg_err.append("O campo %s é obrigatorio" % (col.upper()))

                else:
                    msg_err.append("Erro desconhecido")

            response = {
                "success": False,
                "message": "Não foi possível atualizar a Ação\nDetalhes do erro: %s"
                % ("\n".join(msg_err)),
            }

        else:
            response = {
                "success": True,
                "message": "Voluntario salvo com sucesso",
                "action": self.to_dict(),
            }

        return response

    def delete(self) -> dict:
        try:
            db.session.delete(self)
            db.session.commit()

        except IntegrityError:
            db.session.rollback()
            response = {
                "success": False,
                "message": "Não foi possível excluir a ação",
            }

        else:
            response = {"success": True, "message": "Ação excluida com sucesso!"}

        return response

    def populate_obj(self, data: dict) -> dict:
        for key, value in data.items():
            if key in self.__table__.columns.keys():
                setattr(self, key, value)
