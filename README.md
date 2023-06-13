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


a) Implement Django app with the above schema. Create a corresponding Django Admin interface. (You could add a front end UI if necessary) (8 marks)

b) Implement the following:

✓ Django commands (4 marks)
◦ Create 5 projects
◦ Create 10 households with at least 5 members in each.

✓ Select one assistance project and enlist/enroll at least 3 households that will be targeted and offered $100 cash assistance. (4 marks)

✓ Using a django command, extract a CSV file summary showing all the enrollments in the assistance project and their corresponding cash offers. The file should contain the columns below: (4 marks)
- enrollment_id
- household_id
- household_name
- household_recipient’s full name
- cash_offer
- phone_number

Deliverables
✓ Create a README.md on the project
✓ Requirements.txt
✓ CSV extract
✓ Source code in a zip file.


