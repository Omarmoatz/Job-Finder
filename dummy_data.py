"""Django's command-line utility for administrative tasks."""
import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()



import random
from faker import Faker
from jop.models import Jop, Company, Category

def creat_category(n):
    faker = Faker()
    for x in range(n):
        Category.objects.create(
            name = faker.name()
        )
    print(f'{n} category added')

def create_company(n):
    faker = Faker()
    img = ['job-list1.png','job-list2.png','job-list3.png','job-list4.png']
    for x in range(n):
        Company.objects.create(
            name = faker.company(),
            logo = f'company/{img[random.randint(0,3)]}',
            website = faker.url(),
            email = faker.email(),
            description = faker.text(),
        )
    print(f'{n} company added')

def create_job(n):
    faker = Faker()
    job_nature = ['FullTime','PartTime','Remote','Freelance']
    for x in range(n):
        Jop.objects.create(
            title = faker.name(),
            company = Company.objects.all().order_by('?')[0],
            salary_start = random.randint(2000,3000),
            salary_end = random.randint(3000,4000),
            vacancy = random.randint(0,5),
            experince = random.randint(0,8),
            jop_nature = job_nature[random.randint(0,3)],
            description = faker.sentence(),
            category = Category.objects.all().order_by('?')[0]
        )
    print(f'{n} jop added')


creat_category(5)
create_company(20)
create_job(2000)