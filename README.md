# Snake Game

A simple Snake Game created using Python and the Turtle graphics library. Control the snake using the arrow keys, eat the food to grow longer, and avoid collisions with the walls or your own tail.

## Features
- Classic Snake Game mechanics
- Smooth animation using `turtle` and `time`
- Randomly generated food that extends the snake when eaten
- Scorekeeping system

## Installation
1. Make sure you have Python installed on your system. You can download it from [here](https://www.python.org/downloads/).
2. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/yourusername/your-repository-name.git
    ```
3. Install the required dependencies:
    - `turtle` (pre-installed with Python)
    - `random` (pre-installed with Python)

4. If you haven't already make the custom classes (`newsnake.py`, `food.py`, and `scoreboard.py`), make sure they're in the same directory.

## How to Use
1. Run the `main.py` file:
    ```bash
    python main.py
    ```
2. Control the snake using the arrow keys (Up, Down, Left, Right).
3. The goal is to eat the food (colored squares) to make the snake grow longer.
4. The game ends if the snake hits the walls or collides with its own tail.

## Dependencies
- Python 3.x
- `turtle` library (included with Python)
- `time`, `random` libraries (included with Python)

## Future Improvements
- Add levels and increase difficulty over time.
- Introduce obstacles in the game area.
- Add sound effects and better graphics.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
