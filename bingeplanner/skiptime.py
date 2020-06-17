from datetime import timedelta
import click
import re


class SkipTime(click.ParamType):
    name = 'skiptime'

    def convert(self, value, param, ctx):
        try:
            match = re.search('^(\d{2}):(\d{2})$', value)
            if match:
                minutes = int(match.group(1))
                seconds = int(match.group(2))
                return timedelta(minutes=minutes, seconds=seconds)
            self.fail(
                "expected string of form \"mm:ss\", got "
                f"{value!r}",
                param,
                ctx,
            )
        except TypeError:
            self.fail(
                "expected string of form \"mm:ss\", got "
                f"{value!r} of type {type(value).__name__}",
                param,
                ctx,
            )
