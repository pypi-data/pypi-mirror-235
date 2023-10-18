from typing import Optional

from profyle.application.profyle import profyle
from profyle.domain.trace_repository import TraceRepository
from profyle.infrastructure.sqlite3.repository import SQLiteTraceRepository


class ProfyleMiddleware:
    def __init__(
        self,
        app,
        enabled: bool = True,
        pattern: Optional[str] = None,
        max_stack_depth: int = -1,
        min_duration: int = 0,
        trace_repo: TraceRepository = SQLiteTraceRepository()
    ):
        self.app = app
        self.enabled = enabled
        self.pattern = pattern
        self.max_stack_depth = max_stack_depth
        self.min_duration = min_duration
        self.trace_repo = trace_repo

    def __call__(self, environ, start_response):
        if environ.get("wsgi.url_scheme") == "http" and self.enabled:
            method = environ.get("REQUEST_METHOD", "").upper()
            path = environ.get("REQUEST_URI")
            with profyle(
                name=f"{method} {path}",
                pattern=self.pattern,
                max_stack_depth=self.max_stack_depth,
                min_duration=self.min_duration,
                repo=self.trace_repo
            ):
                return self.app(environ, start_response)
        return self.app(environ, start_response)
