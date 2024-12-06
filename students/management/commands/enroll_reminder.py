import datetime
from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import send_mass_mail
from django.core.management import BaseCommand
from django.db.models import Count
from django.utils import timezone


class Command(BaseCommand):
    help = 'Отправляет напоминание по электронной почте пользователям, \
    зарегистрированным более N дней, которые еще не зачислены ни на какие курсы'

    def add_arguments(self, parser):
        parser.add_argument('--days', dest='days', type=int)

    def handle(self, *args, **options):
        emails = []
        subject = 'Запись на курс'
        date_joined = timezone.now().today() - datetime.timedelta(days=options['days'] or 0)
        users = User.objects.annotate(course_count=Count('courses_joined')).filter(course_count=0,
                                                                                   date_joined__date__lte=date_joined)

        for user in users:
            message = """Здравствуйте! Уважаемый {}!
            Видим, что вы еще не подобрали для себя подходящий курс на нашем сервисе.
            Мы можем вам помочь с выбором?""".format(user.first_name)

            emails.append((subject,
                           message,
                           settings.DEFAULT_FROM_EMAIL,
                           [user.email]))
            send_mass_mail(emails)
            self.stdout.write('Отправление {} напоминания'.format(len(emails)))


