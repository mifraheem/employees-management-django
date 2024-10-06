from django.db import models

# Choices for dropdowns
MARITAL_STATUS_CHOICES = [
    ('Single', 'Single'),
    ('Married', 'Married'),
    ('Divorced', 'Divorced'),
    ('Widowed', 'Widowed'),
]

BLOOD_GROUP_CHOICES = [
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
    ('O+', 'O+'),
    ('O-', 'O-'),
]

EMPLOYMENT_STATUS_CHOICES = [
    ('Permanent', 'Permanent'),
    ('Contract', 'Contract'),
    ('Probation', 'Probation'),
    ('Retired', 'Retired'),
]

EMPLOYMENT_MODE_CHOICES = [
    ('Full-time', 'Full-time'),
    ('Part-time', 'Part-time'),
    ('Consultant', 'Consultant'),
]

DISABILITY_CHOICES = [
    ('None', 'None'),
    ('Physical', 'Physical'),
    ('Visual', 'Visual'),
    ('Hearing', 'Hearing'),
    ('Mental', 'Mental'),
]

# Main Models


class Employee(models.Model):
    name = models.CharField(max_length=255)
    father_name = models.CharField(max_length=255)
    cnic = models.CharField(max_length=13, unique=True)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=[
        ('M', 'Male'), ('F', 'Female'), ('O', 'Other')
    ])
    marital_status = models.CharField(
        max_length=10, choices=MARITAL_STATUS_CHOICES)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES)
    seniority_no = models.CharField(max_length=20)
    personnel_no = models.CharField(max_length=20)
    mobile_no = models.CharField(max_length=15)
    email = models.EmailField()
    photo = models.ImageField(upload_to='employee_photos/')
    remarks = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Address(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    permanent_address = models.TextField()
    correspondence_address = models.TextField()

    def __str__(self):
        return f"Address for {self.employee.name}"


class Employment(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    joining_grade_bps = models.IntegerField()
    current_grade_bps = models.IntegerField()
    present_posting_order_no = models.CharField(max_length=50)
    present_posting_date = models.DateField()
    employment_status = models.CharField(
        max_length=20, choices=EMPLOYMENT_STATUS_CHOICES)
    employment_mode = models.CharField(
        max_length=20, choices=EMPLOYMENT_MODE_CHOICES)
    date_of_first_appointment = models.DateField()
    superannuation_date = models.DateField()
    last_promotion_date = models.DateField()
    present_joining_date = models.DateField()

    def __str__(self):
        return f"Employment details for {self.employee.name}"


class Qualification(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    highest_qualification = models.CharField(max_length=255)
    additional_qualification = models.CharField(
        max_length=255, null=True, blank=True)
    date_of_course = models.DateField(null=True, blank=True)
    course_name = models.CharField(max_length=255, null=True, blank=True)
    pg_specialization = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"Qualification for {self.employee.name}"


class HealthDetails(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    domicile = models.CharField(max_length=100)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES)
    disability = models.CharField(max_length=50, choices=DISABILITY_CHOICES)

    def __str__(self):
        return f"Health details for {self.employee.name}"


class WorkDetails(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    designation = models.CharField(max_length=100)
    working_designation = models.CharField(max_length=100)
    cadre = models.CharField(max_length=100)
    health_facility = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    present_posting_date = models.DateField()
    present_joining_date = models.DateField()

    def __str__(self):
        return f"Work details for {self.employee.name}"


class ContactDetails(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    mobile_no_official = models.CharField(max_length=15)
    fax_no = models.CharField(max_length=20, null=True, blank=True)
    email_official = models.EmailField()

    def __str__(self):
        return f"Contact details for {self.employee.name}"


class PromotionDetails(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    promotion_order_number = models.CharField(max_length=50)
    promotion_joining_date = models.DateField()
    regular_order_number = models.CharField(max_length=50)

    def __str__(self):
        return f"Promotion details for {self.employee.name}"


class Verification(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    is_verified = models.BooleanField(default=False)
    verified_datetime = models.DateTimeField(null=True, blank=True)
    verified_by = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"Verification for {self.employee.name}"
