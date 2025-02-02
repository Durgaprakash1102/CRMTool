from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            # Personal Information
            'first_name', 'middle_name', 'last_name','profile_picture', 'dob', 'place_of_birth', 'father_name',
            'gender', 'marital_status', 'nationality', 'blood_group', 'address', 'city', 'state',
            'zip_code', 'mobile', 'alternate_phone', 'personal_email', 'work_email', 
            'passport_no', 'passport_valid_from', 'passport_valid_upto', 'passport_file_upload',
            'visa_file_upload',

            # PAN Details
            'pan_name', 'pan_number', 'pan_upload_file',

            # Aadhar Details
            'aadhar_name', 'aadhar_number', 'aadhar_file_upload',

            # Provident Fund Information
            'pf_member', 'pf_number', 'pf_withdrawn', 'uan_number', 'uan_confirmed', 'active_visa',

            # Job Information
            'employee_id', 'date_of_joining', 'position', 'department', 'employment_type',
            'reporting_manager', 'job_location', 'work_schedule', 'job_related_documents',

            # Educational Qualifications
            'highest_degree', 'institution_name', 'field_of_study', 'year_of_graduation', 'certifications',

            # Previous Experience
            'previous_company_name', 'previous_job_title', 'previous_work_location', 'previous_exit_date',
            'responsibilities', 'reason_for_leaving',

            # Reference Information
            'reference_1_name', 'reference_1_designation', 'reference_1_company_name', 'reference_1_contact', 'reference_1_email',
            'reference_2_name', 'reference_2_designation', 'reference_2_company_name', 'reference_2_contact', 'reference_2_email',

            # Emergency Contact Information
            'emergency_first_name', 'emergency_middle_name', 'emergency_last_name', 'emergency_relationship',
            'emergency_home_phone', 'emergency_mobile_phone', 'emergency_city', 'emergency_state', 'emergency_zip_code',

            # Bank Information
            'bank_name_on_account', 'bank_account_number', 'bank_name', 'bank_branch_name', 'bank_ifsc_code',
            'bank_branch_address', 'passbook_file_upload',

            # Files Upload for Current Employment
            'offer_letter', 'nda_form', 'btech_memo', 'btech_tc', 'relieving_letter', 'experience_letter', 'payslips',
        ]
        widgets = {
            # Date fields
            'dob': forms.DateInput(attrs={'type': 'date'}),
            'passport_valid_from': forms.DateInput(attrs={'type': 'date'}),
            'passport_valid_upto': forms.DateInput(attrs={'type': 'date'}),
            'date_of_joining': forms.DateInput(attrs={'type': 'date'}),
            'previous_exit_date': forms.DateInput(attrs={'type': 'date'}),

            # TextInput for smaller fields
            'mobile': forms.TextInput(attrs={'type': 'tel'}),
            'alternate_phone': forms.TextInput(attrs={'type': 'tel'}),
            'personal_email': forms.EmailInput(attrs={'type': 'email'}),
            'work_email': forms.EmailInput(attrs={'type': 'email'}),
            'zip_code': forms.TextInput(attrs={'type': 'text'}),

            # File Input for document fields
            'profile_picture': forms.FileInput(),
            'passport_file_upload': forms.FileInput(),
            'visa_file_upload': forms.FileInput(),
            'pan_upload_file': forms.FileInput(),
            'aadhar_file_upload': forms.FileInput(),
            'job_related_documents': forms.FileInput(),
            'certifications': forms.FileInput(),
            'passbook_file_upload': forms.FileInput(),
            'offer_letter': forms.FileInput(),
            'nda_form': forms.FileInput(),
            'btech_memo': forms.FileInput(),
            'btech_tc': forms.FileInput(),
            'relieving_letter': forms.FileInput(),
            'experience_letter': forms.FileInput(),
            'payslips': forms.FileInput(),

            # Dropdown fields for choice fields
            'gender': forms.Select(),
            'marital_status': forms.Select(),
            'employment_type': forms.Select(),
            'pf_member': forms.Select(),
            'pf_withdrawn': forms.Select(),
            'uan_confirmed': forms.Select(),
            'active_visa': forms.Select(),
        }
