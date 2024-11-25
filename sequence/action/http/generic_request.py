class GenericRequest:

    def __init__(self, client, method_type, prefix, token, endpoint, headers, name=None, body=None, **kwargs):
        self.client = client
        self.name = name
        self.method_type = method_type
        self.endpoint = endpoint
        self.headers = headers
        self.body = body
        self.prefix = prefix
        self.token = token
        if name is None:
            self.name = endpoint

    def call(self):
        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        headers.update(self.headers)
        with self.client.rest(
            self.method_type,
            self.prefix + self.endpoint,
            name=self.name,
            json=self.body,
            headers=headers,
            cookies=None,
            allow_redirects=True
        ) as resp:
            return {'last_response': resp}