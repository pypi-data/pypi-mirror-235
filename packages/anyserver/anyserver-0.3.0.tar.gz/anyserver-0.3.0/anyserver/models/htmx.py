from anyserver.models.request import WebRequest


class HtmxRequest():

    def __init__(self, req: WebRequest): self.req = req

    @staticmethod
    def isHTMX(req: WebRequest): return req.header('hx-request', False)

    @property
    def prompt(self): return self.req.header('hx-prompt', '')

    @property
    def triggerName(self): return self.req.header('hx-trigger-name', '')

    @property
    def triggerValue(self): return self.req.input(self.triggerName, '')
