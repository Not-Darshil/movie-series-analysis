# Movie Series Analysis

Welcome to the Movie Series Analysis project! This project allows users to view character networks of various series and submit reviews, which will be analyzed for sentiment. 

## Table of Contents
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Running the Application](#running-the-application)
- [API Documentation](#api-documentation)
- [Contributing](#contributing)
- [License](#license)

## Technologies Used
- **Frontend:** React.js, GSAP
- **Backend:** Node.js, Express
- **Database:** MongoDB
- **Authentication:** JSON Web Tokens (JWT), bcrypt
- **Testing:** [Your preferred testing libraries here] [Not yet decided]

## Getting Started

### Prerequisites
- Node.js (v14 or later)
- npm (Node Package Manager)
- MongoDB
- Git

### Cloning the Repository
1. Open your terminal.
2. Clone the repository using the following command:
   ```bash
   git clone https://github.com/Not-Darshil/movie-series-analysis.git
   ```
3. Navigate into the cloned repository:
    ```
    cd movie-series-analysis
    ```

### Installing Dependencies
1. Install DotEnv package
    ```
    npm install dotenv
    ```
2. Navigate to the frontend directory:
    ```
    cd client
    ```
3. Install frontend dependencies:
    ```
    npm install
    ```
4. Go back to the root directory:
    ```
    cd ..
    ```
5. Navigate to the backend directory:
    ```
    cd server
    ```
6. Install backend dependencies:
    ```
    npm install
    ```

## Project Structure
```
/movie-series-analysis
│
├── /client             # Frontend (React)
│   ├── /public         # Static files (HTML, images, etc.)
│   ├── /src            # React source files
│   └── package.json    # React dependencies
│
├── /server             # Backend (Node.js with Express)
│   ├── /config         # Configuration files
│   ├── /controllers    # API controllers
│   ├── /models         # Database models
│   ├── /routes         # API routes
│   ├── /middleware     # Authentication and other middleware
│   └── app.js          # Main server file
│
├── /tests              # Tests (both frontend and backend)
│
├── .gitignore          # Ignored files for Git
├── README.md           # Project overview and documentation
└── docker-compose.yml  # Docker setup (optional)

```

## Running the Application

#### Running the Frontend
In the /client directory, start the React application:
    ```
    npm start
    ```
The frontend will be accessible at http://localhost:3000.

#### Running the Backend
In the /server directory, start the Node.js server:
    ```
    npm start
    ```
The backend API will be accessible at http://localhost:5000.

#### Running Both Applications
You can also run both the frontend and backend simultaneously from the root directory by using:
    ```
    npm start
    ```

## API Documentation
Provide documentation for your API endpoints here[Not yet decided], including:

GET /api/movies - Retrieves all movies.
<br>
POST /api/reviews - Submits a review.


## Contributing
If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
1. Create your feature branch (git checkout -b feature/AmazingFeature).
1. Commit your changes (git commit -m 'Add some AmazingFeature').
1. Push to the branch (git push origin feature/AmazingFeature).
1. Open a Pull Request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.



