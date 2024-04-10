import tkinter as tk

# Constants
WIDTH, HEIGHT = 400, 300
BALL_RADIUS = 20
DX, DY = 2, 2  # Movement increments

# Function to move the ball
def move_ball():
    global x, y, DX, DY
    # Move the ball
    canvas.move(ball, DX, DY)
    x += DX
    y += DY
    # Bounce off the walls
    if x <= 0 or x >= WIDTH - BALL_RADIUS * 2:
        DX *= -1
    if y <= 0 or y >= HEIGHT - BALL_RADIUS * 2:
        DY *= -1
    # Schedule the move_ball function to be called again after a delay
    root.after(10, move_ball)

# Create the Tkinter window
root = tk.Tk()
root.title("Animation Example")

# Create the canvas
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
canvas.pack()

# Create the ball
x, y = WIDTH // 2, HEIGHT // 2  # Initial position
ball = canvas.create_oval(x, y, x + BALL_RADIUS * 2, y + BALL_RADIUS * 2, fill="red")

# Start the animation
move_ball()

# Run the Tkinter event loop
root.mainloop()
