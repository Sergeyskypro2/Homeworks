from yougile import Yougile


def test_get_auth_key():
    auth = Yougile()
    response = auth.get_auth_key()
    return response["key"]


def test_get_project():
    get_project = Yougile()
    body = get_project.get_project()
    len(body['content'])


def test_create_project():
    get_project = Yougile()
    body = get_project.get_project()
    len_before = len(body['content'])

    project = Yougile()
    result = project.create_project()
    new_id = result["id"]
    body = get_project.get_project()
    len_after = len(body['content'])

    assert len_after > len_before
    assert body['content'][-1]["id"] == new_id


def test_put_project():
    project = Yougile()
    res = project.get_project()
    id = res['content'][-1]['id']

    project = Yougile()
    new_title = project.put_project(id)

    new_title = Yougile()
    result = new_title.new_title_project(id)
    assert result['content'][-1]["id"] == id
    assert result['content'][-1]["title"] == new_title