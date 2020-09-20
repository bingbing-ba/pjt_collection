import os

from django.core.management.base import BaseCommand, CommandError
from pathlib import Path
from .run_pjt import start_multiprocessing


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('port', type=int)
        parser.add_argument('pjt', type=str)

    def handle(self, *args, **options):
        pjt = options.get('pjt')
        port = options.get('port')
        start_multiprocessing(pjt)
        self.stdout.write(
            self.style.SUCCESS(f'''
            =====================================
            MAIN SERVER IS RUNNING AT PORT {port}

            URL 🔗 http://127.0.0.1:8080/{pjt}
            =====================================
            ''')
        )