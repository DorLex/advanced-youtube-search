class Parser:
    def __init__(self, item: dict):
        self.item = item

    @property
    def content_type(self) -> str:
        kind: str = self.item['id']['kind']
        return kind.split('#')[1]

    @property
    def title(self) -> str:
        return self.item['snippet']['title']

    @property
    def description(self) -> str:
        return self.item['snippet']['description']
