# Primeiro vamos imaginar que estamos fazendo uma classe
# para se conectar ao banco de dados
from rich import print


class DataBase:
    """
    Esse é o próprio 'Banco de Dados'.
    """

    def __init__(self, *args, **kwargs):

        self.__is_conected: boll = False

    @property
    def is_connected(self) -> bool:
        return self.__is_conected

    @is_connected.setter
    def is_connected(self, new_status: bool) -> None:
        self.__is_conected = new_status


class ConnectToDataBase(DataBase):

    # Instância do objeto que será retornado
    _connection = None

    def __init__(self, *args, **kwargs):
        super(ConnectToDataBase, self).__init__(*args, **kwargs)

        pass

    @classmethod
    def get_instance(cls):

        # Se a intância estiver vazia então ele irá criar uma instância.
        if cls._connection == None:
            cls._connection = ConnectToDataBase()

        # Retorna a instância.
        return cls._connection


if __name__ == "__main__":

    # Fazendo a conecção
    connection: ConnectToDataBase = ConnectToDataBase.get_instance()
    print(connection)

    connection_2: ConnectToDataBase = ConnectToDataBase.get_instance()

    # Verificnaod se eleas são a mesma instância
    print(
        f"Id connection == Id connection_2 => {id(connection) == id(connection_2)}"
    )  # True

    print(connection.is_connected)  # False

    # Mudando a conecção o estatus do Primeiro
    connection.is_connected = True

    # Verificando no segundo
    print("Connection_2: ", connection_2.is_connected)
