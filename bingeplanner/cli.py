import os
import click
import enzyme
import re
import datetime


@click.command()
@click.argument('episodes', nargs=1)
@click.option('--fill', default=2)
@click.option('--regex', default=' <i> .*\.mkv')
def cli(episodes, fill, regex):
    episode_indices = parse_range(episodes, fill)

    delta = datetime.timedelta()
    for root, dirs, files in os.walk("."):
        for filename in files:
            if any(re.search(regex.replace('<i>', index), filename) for index in episode_indices):
                path = os.path.join(root, filename)
                with open(path, 'rb') as f:
                    mkv = enzyme.MKV(f)
                    delta += mkv.info.duration
    print(td_format(delta))


def parse_range(input, range_fill):
    result = []
    for part in input.split(','):
        if '-' in part:
            a, b = part.split('-')
            a, b = int(a), int(b)
            result.extend([str(i).zfill(range_fill) for i in range(a, b + 1)])
        else:
            a = part
            result.append(a)
    return result


def td_format(td_object):
    seconds = int(td_object.total_seconds())
    periods = [
        ('year',        60*60*24*365),
        ('month',       60*60*24*30),
        ('day',         60*60*24),
        ('hour',        60*60),
        ('minute',      60),
        ('second',      1)
    ]

    strings = []
    for period_name, period_seconds in periods:
        if seconds > period_seconds:
            period_value, seconds = divmod(seconds, period_seconds)
            has_s = 's' if period_value > 1 else ''
            strings.append("%s %s%s" % (period_value, period_name, has_s))

    return ", ".join(strings)


if __name__ == '__main__':
    cli()
