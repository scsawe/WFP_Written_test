# WFP_Written_test
Project to implement a beneficiary registration and cash transfers management application and add a couple of django management commands

Case study

WFP has several assistance programmes (assistance projects) that are used to periodically offer cash assistance/transfers to the targeted beneficiaries. WFP is
intending to do registrations of about 10 families (households) affected by drought where each household will be offered $100 monthly to cater for any food commodity purchases at the several defined WFP retailers/vendors.

Given a Django application with the following schema:

• Household – Consider this a composition of family members. A household
contains several members.

• Person – A member of a household. Every member belongs to one
household.

• Assistance Project – A programme that is used to offer cash assistance/aid to beneficiaries. Each household is usually targeted and offered cash monthly to cater for food commodity purchases at the retailers.

• Enrollment – Refers to any household that is targeted in the assistance project.

Schema
• household
- id
- name
- location

• person
- first_name
- last_name
- household → foreign key to household
- phone_number
- is_recipient – boolean defining whether the person is the designated recipient of the household. He/she will receive the case on behave of the household.
- 
• assitance_project
- id
- name
- start_date
- end_date

• enrollment
- id
- assistance_project → foreign key to assistance_project
- household → foreign key to household
- cash_offer

a) Implement Django app with the above schema. Create a corresponding Django Admin interface. (You could add a front end UI if necessary) (8 marks)

b) Implement the following:

✓ Django commands (4 marks)
◦ Create 5 projects
◦ Create 10 households with at least 5 members in each.

✓ Select one assistance project and enlist/enroll at least 3 households that will be targeted and offered $100 cash assistance. (4 marks)

✓ Using a django command, extract a CSV file summary showing all the enrollments in the assistance project and their corresponding cash offers. The file should contain the columns below: (4 marks)

