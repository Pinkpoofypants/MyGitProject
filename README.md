# MyGitProject
Assignment 2 for computer concepts COMP1243

1. Names entered in shared spreadsheet

Aaleyah Evans (leyah242) - 100159942

Charlie Allaby (Pinkpoofypants) - 100161606

3. Problem:

We wanted to create a rock, paper, scissors game in python. 

4. Roles in project
Aaleyah: Front end and driver

Charlie: Back end and rock paper scissors logic

1. Names entered in a shared spreadsheet
Aaleyah Evans - (Leyah242) - 100159912
Charlie Allaby (Pinkpoofypants) - 100161606

2. Problem:
Develop a **Rock, Paper, Scissors** game where a user plays against the computer in a command-line interface (CLI). The game should:  
- Allow the user to enter "rock," "paper," or "scissors."  
- Randomly generate the computer’s choice.  
- Compare choices and determine the winner based on standard rules:  
  - Rock beats Scissors  
  - Scissors beats Paper  
  - Paper beats Rock  
  - If both choices are the same, it's a tie.  
- Allow the user to play multiple rounds until they choose to quit.  

The project should also demonstrate **collaborative coding** using GitHub, including **branching, pull requests, and commits** to manage contributions from multiple team members.

3. Roles in the project
Aaleyah:

Charlie:


7. Coding Task
Backend Development (Charlie)
- Implemented the core game logic using object-oriented programming (OOP).  
- Created classes (`rock`, `paper`, `scissors`) inheriting from a base class `rpsObject`, each with a `value` and a `weakness` attribute.  
- Developed the `rpsMake(choice)` function to return the corresponding object based on the user or computer’s choice.  
- Implemented the `randomChoice()` function to allow the computer to randomly select between rock, paper, and scissors.  
- Built the `testWin(computer, player)` function to determine the winner based on the game's rules:  
  - Returns `1` if the player wins.  
  - Returns `2` if the computer wins.  
  - Returns `0` if it’s a tie.  

This backend logic ensures that the game operates correctly by processing user input and computing results efficiently.

Frontend Development (Aaleyah)
- Designed the command-line interface (CLI) for user interaction.  
- Provided clear game instructions and options for user input.  
- Allowed users to enter their choice (`r`, `p`, `s`) or quit the game at any time.  
- Ensured smooth game flow by handling user input validation before passing it to the backend logic.  

This separation of frontend and backend allowed for modular design, making it easier to manage and collaborate on the project using GitHub.  

9. Version Control Workflow:

To effectively collaborate on this project, we established a structured version control workflow using GitHub. Our repository contained two main branches:  

1. **`mygithubproject.1` Branch** – This branch focused on implementing the core functionality of the Rock, Paper, Scissors game. It contained the logic for user input, computer-generated choices, and determining the winner.  

2. **`frontend` Branch** – This branch served as the driver class, handling user interaction and executing the game based on the logic implemented in the first branch.  

Each team member worked on their assigned task within their respective branches, making commits as they progressed. Once the changes were tested and verified, we merged the `frontend` branch with `mygithubproject.1`, ensuring a seamless integration of functionality and user interaction. This workflow allowed us to maintain an organized structure while efficiently tracking and managing contributions.

