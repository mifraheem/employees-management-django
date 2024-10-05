from django.shortcuts import HttpResponse
from faker import Faker
from .models import Employee, Address, Employment, Qualification, HealthDetails, WorkDetails
import random
from datetime import date

fake = Faker('en_PK')
# Helper function to generate Pakistani phone numbers


def generate_pakistani_phone_number():
    # Pakistani mobile network codes
    mobile_network_code = random.choice(
        ['300', '301', '302', '303', '304', '305', '306', '307', '308', '309'])

    # Generate a 7-digit random number for the phone
    phone_number = ''.join([str(random.randint(0, 9)) for _ in range(7)])

    # Return the formatted number: +92 XXX XXXXXXX
    return f'+92 {mobile_network_code} {phone_number}'


def add_dummy_employees(request):
    for _ in range(10):
        # Generate fake employee data
        name = fake.first_name_male()

        father_name = fake.first_name_female() + " " + fake.last_name()
        cnic = fake.unique.random_number(digits=13, fix_len=True)
        dob = fake.date_of_birth(minimum_age=20, maximum_age=60)
        gender = 'M'
        marital_status = random.choice(['Single', 'Married'])
        blood_group = random.choice(
            ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-'])
        seniority_no = fake.random_number(digits=5)
        personnel_no = fake.random_number(digits=5)
        mobile_no = generate_pakistani_phone_number()
        email = fake.email()

        # Create the Employee
        employee = Employee.objects.create(
            name=name,
            father_name=father_name,
            cnic=cnic,
            date_of_birth=dob,
            gender=gender,
            marital_status=marital_status,
            blood_group=blood_group,
            seniority_no=seniority_no,
            personnel_no=personnel_no,
            mobile_no=mobile_no,
            email=email,
            photo=None
        )

        # Create Address
        Address.objects.create(
            employee=employee,
            permanent_address=fake.address(),
            correspondence_address=fake.address()
        )

        # Create Employment details
        Employment.objects.create(
            employee=employee,
            joining_grade_bps=random.randint(1, 20),
            current_grade_bps=random.randint(1, 20),
            present_posting_order_no=fake.random_number(digits=6),
            present_posting_date=fake.date_this_decade(),
            employment_status=random.choice(
                ['Permanent', 'Contract', 'Probation']),
            employment_mode=random.choice(['Full-time', 'Part-time']),
            date_of_first_appointment=fake.date_this_decade(),
            superannuation_date=fake.date_this_decade(),
            last_promotion_date=fake.date_this_decade(),
            present_joining_date=fake.date_this_decade(),
        )

        # Create Qualification
        Qualification.objects.create(
            employee=employee,
            highest_qualification=random.choice(['BSc', 'MSc', 'PhD']),
            additional_qualification=random.choice(
                ['Diploma', 'Certification']),
            date_of_course=fake.date_this_decade(),
            course_name=fake.job(),
            pg_specialization=fake.bs()
        )

        # Create Health Details
        HealthDetails.objects.create(
            employee=employee,
            domicile=fake.state(),
            blood_group=blood_group,
            disability=random.choice(['None', 'Physical', 'Visual', 'Hearing'])
        )

        # Create Work Details
        WorkDetails.objects.create(
            employee=employee,
            designation=fake.job(),
            working_designation=fake.job(),
            cadre=fake.company(),
            health_facility=fake.company(),
            department=fake.bs(),
            present_posting_date=fake.date_this_decade(),
            present_joining_date=fake.date_this_decade()
        )

    return HttpResponse("10 Dummy Employees Added Successfully")
