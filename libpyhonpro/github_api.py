import requests


def buscar_avatar(usuario):
    """
    Busca o avatar de um usuário no Github

    :param usuario: str como o nome do usuário no github
    :return: str com o link do avatar
    """
    url = f'https://api.github.com/users/{usuario}'
    resp = requests.get(url)
    resp.json()
    return resp.json()['avatar_url']


if __name__ == '__main__':
    print(buscar_avatar('gelhen'))
