# Wordle Application

Welcome to DOJO! Over the next 4 weeks, we will be building a multiplayer online version of the popular word game, Wordle. 
Each week, we'll focus on different aspects of the application, gradually building up to a fully functional game.


## Getting Started
- Run docker-compose up

## Project Overview

Our version of Wordle allows players to guess a hidden word, with feedback given for each guess in the form of colored 
tiles, indicating when letters match or occupy the correct position. Our multiplayer twist allows users to play against 
each other in real-time.

## Week 6: Setting Up the Project and Backend Development

### Objectives:
- Design and implement the MySQL database schema for storing user information, game states, and word lists, learn 
  about migrations.
- Develop the FastAPI backend to handle user authentication, game logic, and database operations.
- Set up Login, Registration, Leaderboard, and Game endpoints.
- Create basic HTML/CSS for the frontend.

### Tasks:
1. Design the MySQL database schema and implement it.
2. Create FastAPI endpoints for user registration, login, and leaderboard.
3. Implement the game logic for generating daily words and validating guesses.

## Week 7: Frontend Development and User Interface

### Objectives:
- Develop the frontend using JavaScript, CSS, and HTML.
- Implement a responsive user interface for the game.
- Integrate the frontend with the FastAPI backend using AJAX for data fetching and submission.

### Tasks:
1. Design and implement the game interface, including the keyboard and guess grid.
2. Create JavaScript functions to handle user inputs, game logic on the client side, and display feedback.
3. Style the application using CSS to ensure a responsive and attractive design.
4. Connect the frontend to the backend API for user authentication, game interactions, and retrieving game results.

## Week 8: Real-time Gameplay with WebSockets

### Objectives:
- Implement real-time multiplayer functionality using WebSockets.
- Enable live updates for players' guesses and game progress.

### Tasks:
1. Integrate WebSockets with the FastAPI backend to handle real-time communication.
2. Modify the frontend to support real-time gameplay, allowing multiple users to play and see each other's progress live.
3. Ensure synchronization of game state across all connected clients.

## Week 9: Testing and Debugging

### Objectives:
- Continue with multiplayer functionality using WebSockets. 
- Perform comprehensive testing to identify and fix bugs.
- Optimize performance and ensure security best practices are followed.

### Tasks:
1. Write and run unit tests for the backend to cover user authentication, game logic, and database operations.
2. Conduct manual testing of the frontend, focusing on user experience and interface responsiveness.
3. Identify and fix bugs reported during testing.
4. Review and optimize the application for performance and security.

## Week 10: Deployment and Final Touches

### Objectives:
- Deploy the application to a production environment.
- Add final touches and prepare for launch.

### Tasks:
1. Prepare the application for deployment, including configuration for production databases and environment variables.
2. Deploy the application to a cloud platform or server.
3. Conduct final testing in the production environment to ensure everything works as expected.
