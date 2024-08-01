from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:password@localhost/fastapi"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

"""
This PR contains the implementation of `[GET] /api/v1/organization/{org_id}/users` [PROTECTED Endpoint]

## Description

Added functionality for retrieving all users in an organization. This includes creating an endpoint `/api/v1/organization/{org_id}/users` that fetches all users in an organization from the database. The endpoint returns a list of users, each containing details such as first_name, last_name, username, email, etc.

## Related Issue (Link to issue ticket)
This is an implementation of an open issue #332 

## Motivation and Context

This feature  is required to provide an endpoint for users who are members of an organization to view all other users in the organization.

## How Has This Been Tested?

The new functionality has been tested using pytest, FastAPI test client, Postman and manual testing. Tests include:
- Retrieving all users in an organization the user belongs to
- Test cases for authentication and authorization
- Test cases for error scenarios (invalid UUID, organization not found, etc.)

Test environment:
- PostgreSQL database for storing blog information.
- Mock database setup using pytest for isolated testing.
- Test client setup using FastAPI for API endpoint testing.

## Screenshots (if appropriate - Postman, etc):

###Successful response - Postman
![postman](https://github.com/user-attachments/assets/6ef5a2e5-88cb-4e12-9181-05b44155a584)

###FastAPI - OpenAPI
![OpenAPI](https://github.com/user-attachments/assets/72adecb1-4b0c-4d53-ac92-4574d568cb9f)

## Types of changes
- [ ] Bug fix (non-breaking change which fixes an issue)
- [x] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to change)
      ​
## Checklist:
- [x] My code follows the code style of this project.
- [ ] My change requires a change to the documentation.
- [ ] I have updated the documentation accordingly.
- [x] I have read the **CONTRIBUTING** document.
- [x] I have added tests to cover my changes.
- [x] All new and existing tests passed.
"""
