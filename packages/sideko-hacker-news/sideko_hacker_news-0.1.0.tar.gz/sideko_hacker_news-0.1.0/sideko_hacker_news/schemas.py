from typing import List, Optional, Any, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class GetUpdatesJSONResponse:
    """Item response"""
    """Changed items"""
    items: Optional[List[int]]
    """Changed profiles"""
    profiles: Optional[List[str]]

    def __init__(self, items: Optional[List[int]], profiles: Optional[List[str]]) -> None:
        self.items = items
        self.profiles = profiles

    @staticmethod
    def from_dict(obj: Any) -> 'GetUpdatesJSONResponse':
        assert isinstance(obj, dict)
        items = from_union([lambda x: from_list(from_int, x), from_none], obj.get("items"))
        profiles = from_union([lambda x: from_list(from_str, x), from_none], obj.get("profiles"))
        return GetUpdatesJSONResponse(items, profiles)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.items is not None:
            result["items"] = from_union([lambda x: from_list(from_int, x), from_none], self.items)
        if self.profiles is not None:
            result["profiles"] = from_union([lambda x: from_list(from_str, x), from_none], self.profiles)
        return result


class Item:
    """Item response"""
    by: str
    dead: Optional[bool]
    deleted: Optional[bool]
    descendants: Optional[int]
    id: int
    kids: Optional[List[int]]
    parent: Optional[int]
    parts: Optional[List[int]]
    poll: Optional[int]
    score: Optional[int]
    text: Optional[str]
    time: int
    title: Optional[str]
    type: str
    url: Optional[str]

    def __init__(self, by: str, dead: Optional[bool], deleted: Optional[bool], descendants: Optional[int], id: int, kids: Optional[List[int]], parent: Optional[int], parts: Optional[List[int]], poll: Optional[int], score: Optional[int], text: Optional[str], time: int, title: Optional[str], type: str, url: Optional[str]) -> None:
        self.by = by
        self.dead = dead
        self.deleted = deleted
        self.descendants = descendants
        self.id = id
        self.kids = kids
        self.parent = parent
        self.parts = parts
        self.poll = poll
        self.score = score
        self.text = text
        self.time = time
        self.title = title
        self.type = type
        self.url = url

    @staticmethod
    def from_dict(obj: Any) -> 'Item':
        assert isinstance(obj, dict)
        by = from_str(obj.get("by"))
        dead = from_union([from_bool, from_none], obj.get("dead"))
        deleted = from_union([from_bool, from_none], obj.get("deleted"))
        descendants = from_union([from_int, from_none], obj.get("descendants"))
        id = from_int(obj.get("id"))
        kids = from_union([lambda x: from_list(from_int, x), from_none], obj.get("kids"))
        parent = from_union([from_int, from_none], obj.get("parent"))
        parts = from_union([lambda x: from_list(from_int, x), from_none], obj.get("parts"))
        poll = from_union([from_int, from_none], obj.get("poll"))
        score = from_union([from_int, from_none], obj.get("score"))
        text = from_union([from_str, from_none], obj.get("text"))
        time = from_int(obj.get("time"))
        title = from_union([from_str, from_none], obj.get("title"))
        type = from_str(obj.get("type"))
        url = from_union([from_str, from_none], obj.get("url"))
        return Item(by, dead, deleted, descendants, id, kids, parent, parts, poll, score, text, time, title, type, url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["by"] = from_str(self.by)
        if self.dead is not None:
            result["dead"] = from_union([from_bool, from_none], self.dead)
        if self.deleted is not None:
            result["deleted"] = from_union([from_bool, from_none], self.deleted)
        if self.descendants is not None:
            result["descendants"] = from_union([from_int, from_none], self.descendants)
        result["id"] = from_int(self.id)
        if self.kids is not None:
            result["kids"] = from_union([lambda x: from_list(from_int, x), from_none], self.kids)
        if self.parent is not None:
            result["parent"] = from_union([from_int, from_none], self.parent)
        if self.parts is not None:
            result["parts"] = from_union([lambda x: from_list(from_int, x), from_none], self.parts)
        if self.poll is not None:
            result["poll"] = from_union([from_int, from_none], self.poll)
        if self.score is not None:
            result["score"] = from_union([from_int, from_none], self.score)
        if self.text is not None:
            result["text"] = from_union([from_str, from_none], self.text)
        result["time"] = from_int(self.time)
        if self.title is not None:
            result["title"] = from_union([from_str, from_none], self.title)
        result["type"] = from_str(self.type)
        if self.url is not None:
            result["url"] = from_union([from_str, from_none], self.url)
        return result


class User:
    """User object"""
    """The user's optional self-description. HTML"""
    about: Optional[str]
    """Creation date of the user, in Unix Time"""
    created: Optional[int]
    id: Optional[str]
    """The user's karma"""
    karma: Optional[int]
    submitted: Any

    def __init__(self, about: Optional[str], created: Optional[int], id: Optional[str], karma: Optional[int], submitted: Any) -> None:
        self.about = about
        self.created = created
        self.id = id
        self.karma = karma
        self.submitted = submitted

    @staticmethod
    def from_dict(obj: Any) -> 'User':
        assert isinstance(obj, dict)
        about = from_union([from_str, from_none], obj.get("about"))
        created = from_union([from_int, from_none], obj.get("created"))
        id = from_union([from_str, from_none], obj.get("id"))
        karma = from_union([from_int, from_none], obj.get("karma"))
        submitted = obj.get("submitted")
        return User(about, created, id, karma, submitted)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.about is not None:
            result["about"] = from_union([from_str, from_none], self.about)
        if self.created is not None:
            result["created"] = from_union([from_int, from_none], self.created)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.karma is not None:
            result["karma"] = from_union([from_int, from_none], self.karma)
        if self.submitted is not None:
            result["submitted"] = self.submitted
        return result


def get_updates_json_response_from_dict(s: Any) -> GetUpdatesJSONResponse:
    return GetUpdatesJSONResponse.from_dict(s)


def get_updates_json_response_to_dict(x: GetUpdatesJSONResponse) -> Any:
    return to_class(GetUpdatesJSONResponse, x)


def item_from_dict(s: Any) -> Item:
    return Item.from_dict(s)


def item_to_dict(x: Item) -> Any:
    return to_class(Item, x)


def user_from_dict(s: Any) -> User:
    return User.from_dict(s)


def user_to_dict(x: User) -> Any:
    return to_class(User, x)
