# Project Setup Guide

This will help you set up and run the assignment project on your local machine using Docker Compose.

## Prerequisites

- **Docker**: Ensure Docker is installed and running on your machine.

## Setup Instructions

```bash
# 1. Clone the Repository
git clone https://github.com/mstomar698/german
# 2. Create .env files from .env.example files
cp backend/news_stories/.env.example backend/news_stories/.env
cp frontend/.env.example frontend/.env
# 3. Build and Run the Project
docker-compose up --build
# 4. Navigate to localhost:3000 in your browser
```

## API Documentation
 
### Backend
- **API Documentation**: [http://localhost:3000/api-docs](http://localhost:3000/api-docs)
> Note: The API documentation is accessible only when the project is running. <br />
> Note: The default documenation provided by Swagger UI is used for API documentation. 

### Frontend
- **Frontend**: [http://localhost:3000](http://localhost:3000)
> Note: First Page will have latest 10 Stories from Hacker News API. <br />
> Note: On Clicking <u>Title</u>, it will show original story from Hacker News. <br />
> Note: On Clicking <u>read more</u> button, it will show detail page of the story. <br />
> Note: On Clicking <u>back</u> button, it will take you back to the first page.  <br />

## Project Structure

```bash
.<root-directory>
    ├──docker-compose.yml
    ├──README.md
    ├── backend
       ├── docker-compose.yml
       ├──news_stories
          ├── dependencies
          ├── domain
          ├── routes
          ├── schemas
          ├── tests
          ├── Dockerfile
          ├──.env
          ├──main.py
          ├──settings.py
          ├──requirements.txt
    ├── frontend
        ├──Dockefile
        ├──.env
        ├──package.json
        ├──tailwind.config.js
        ├──postcss.config.js
        ├──public
        ├──src
            ├──components
            ├──pages
            ├──App.js
            ├──App.test.jsx
            ├──index.js
            ├──index.css
            ├──setupTests.js
```

## Tech Stack

```
- Backend: FastAPI
- Bakcned-Tests: Pytest
- Frontend: React
- Frontend-Tests: Jest
- Cache: Redis
- Containerization: Docker
```

## Testing
    
```bash
### Backend
docker-compose up app-news-stories-tests

### Frontend
docker-compose up frontend-tests

### Combined
docker-compose up frontend-tests app-news-stories-tests
```

## Authors
> This Assignment was put together by Mayank Singh Tomar