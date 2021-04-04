import bonobo


def extract():
    """Placeholder, change, rename, remove... """
    yield 'hello'
    yield 'world'


def transform(*args):
    """Placeholder, change, rename, remove... """
    yield tuple(
        map(str.title, args)
    )


def load(*args):
    """Placeholder, change, rename, remove... """
    print(*args)


def get_graph(**options):
    """
    This function builds the graph that needs to be executed.

    :return: bonobo.Graph

    """
    graph = bonobo.Graph()
    graph.add_chain(extract, transform, load)

    return graph


def get_services(**options):
    """
    This function builds the services dictionary, which is a simple dict of names-to-implementation used by bonobo
    for runtime injection.

    It will be used on top of the defaults provided by bonobo (fs, http, ...). You can override those defaults, or just
    let the framework define them. You can also define your own services and naming is up to you.

    :return: dict
    """
    return {}


def run(**options):
    bonobo.run(
        get_graph(**options),
        services=get_services(**options)
    )


# The __main__ block actually execute the graph.
if __name__ == '__main__':
    """Main entrypoint"""
    parser = bonobo.get_argument_parser()
    with bonobo.parse_args(parser) as options:
        run(**options)