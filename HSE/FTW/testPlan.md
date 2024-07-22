# Test Plan for Fit To Work (FTW) Module

## Project Name
Fit To Work (FTW) Module for Coal Company HSE Integration

## Introduction
- **Purpose**: To ensure the FTW module meets all functional and non-functional requirements.
- **Scope**: Testing the functionalities for Admin, PJO, and Doctor roles, as well as API endpoints.
- **Objectives**: Verify the functionality, performance, security, and usability of the FTW module.

## Test Items
- Admin functionalities: Login, add critical items, add penyakit lainnya, add clinic, add doctor, see MCU results.
- PJO functionalities: Login, see MCU results.
- Doctor functionalities: Login, change password, input MCU result, see MCU results.
- API endpoints: GET MCU results, POST MCU results.

## Testing Strategy
- **Test Levels**: Unit testing, integration testing, system testing, acceptance testing.
- **Test Types**: Functional, performance, security, usability.
- **Approach**: Combination of manual and automated testing, using both black-box and white-box techniques.

## Test Deliverables
- Test plan document
- Test Cases and Test scripts
- Test Data
- Test reports

## Testing Schedule
- Preparation: 1 week
- Execution: 2 weeks
- Reporting: 1 week

## Resources
- **Personnel**: 2 QA Engineers, 1 Test Manager, 1 Developer, 1 Product Manager
- **Environment**: Test server, staging server, production server
- **Tools**: Selenium, Postman, JMeter, OWASP ZAP, Jenkins

## Risk Management
- Delays in test environment setup: Mitigate by early setup and frequent checks.
- Incomplete test data: Mitigate by preparing comprehensive test data in advance.

## Exit Criteria
- All test cases executed with at least 95% pass rate
- No critical or high-severity defects open

## Approval
- Signed off by QA Lead, Product Manager, and Development Lead
