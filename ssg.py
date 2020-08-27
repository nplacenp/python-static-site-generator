import typer

from ssg.site import Site

def main(source='content', dest='dist'):

    config = {
        'source': source,
        'dest': dest,
    }

    New_Site = Site(source, dest)
    New_Site.build(main)