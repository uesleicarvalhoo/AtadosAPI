import json

def test_voluntary_get_all(client):
    header = {"Content-Type": "application/json", "Accept": "application/json"}

    response = client.get("/api/voluntary/", headers=header)
    response_data = response.json
    with open("response.json", "w") as r:
        json.dump(response_data, r)
    assert response.status_code == 200
    assert type(response_data) == list

def test_voluntary_post(client):
    header = {"Content-Type": "application/json", "Accept": "application/json"}
    payload = {
        "name": "Voluntario com nome alterado",
        "surname": "Novo sobrenome",
        "district": "Fazenda Grande do Retiro",
        "city": "Salvador"
    }

    response = client.post("/api/voluntary/", headers=header, data=json.dumps(payload))
    response_data = response.json

    assert response.status_code == 200
    assert response_data["success"]

    for key, value in response_data["voluntary"]:
        if key in payload.keys():
            assert payload.get(key) == value


def test_voluntary_get(client):
    header = {"Content-Type": "application/json", "Accept": "application/json"}
    response = client.get("/api/voluntary/1", headers=header)
    response_data = response.json

    assert response.status_code == 200
    assert response_data["success"]

    response = client.get("/api/voluntary/100")
    response_data = response.json

    assert response.status_code == 200
    assert not response_data["success"]


def test_voluntary_update(client):
    header = {"Content-Type": "application/json", "Accept": "application/json"}
    payload = {"name":"Nome atualizado"}
    response = client.put("/api/voluntary/1", headers=header, data=json.dumps(payload))
    response_data = response.json

    assert response_data["success"]
    assert response["voluntary"]["name"] == payload["name"]


def test_voluntary_delete(client):
    header = {"Content-Type": "application/json", "Accept": "application/json"}
    response = client.delete("/api/voluntary/1")
    response_data = response.json

    assert response_data["success"]

    response = client.get("/api/voluntary/1")
    assert not response.json["success"]
