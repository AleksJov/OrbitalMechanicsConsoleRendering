import math
import time
import sys

class ConsoleRender:

    @staticmethod
    def render_console(x_values, y_values, sun_x, sun_y,
                       width=50, height=20):
        # Include the full trail and Sun when choosing the display scale.
        all_x = list(x_values) + [sun_x]
        all_y = list(y_values) + [sun_y]

        max_x = max(abs(value) for value in all_x) or 1
        max_y = max(abs(value) for value in all_y) or 1
        scale = min((width - 1) / (2 * max_x),
                    (height - 1) / (2 * max_y))

        grid = [[" " for _ in range(width)] for _ in range(height)]

        def to_cell(x, y):
            col = round(width / 2 + x * scale)
            row = round(height / 2 - y * scale)
            return row, col

        # Trail
        for x, y in zip(x_values, y_values):
            row, col = to_cell(x, y)
            if 0 <= row < height and 0 <= col < width:
                grid[row][col] = "."

        # Sun and current planet
        row, col = to_cell(sun_x, sun_y)
        if 0 <= row < height and 0 <= col < width:
            grid[row][col] = "☼"

        row, col = to_cell(x_values[-1], y_values[-1])
        if 0 <= row < height and 0 <= col < width:
            grid[row][col] = "O"

        print("\033[H\033[J", end="")  # Clear/redraw terminal
        print("\n".join("".join(row) for row in grid))

    @staticmethod
    def make_frame(x_values, y_values, sun_x, sun_y,
                   width=50, height=20):

        AU = 1.496e11

        all_x = list(x_values) + [sun_x]
        all_y = list(y_values) + [sun_y]

        max_x = max(abs(value) for value in all_x) or 1
        max_y = max(abs(value) for value in all_y) or 1
        scale = min((width - 1, height - 1)) / (2 * 1.2 * AU)

        grid = [[" " for _ in range(width)] for _ in range(height)]

        def to_cell(x, y):
            col = round(width / 2 + x * scale)
            row = round(height / 2 - y * scale)
            return row, col

        # Trail
        for x, y in zip(x_values, y_values):
            row, col = to_cell(x, y)
            if 0 <= row < height and 0 <= col < width:
                grid[row][col] = "."

        # Sun and current planet
        row, col = to_cell(sun_x, sun_y)
        if 0 <= row < height and 0 <= col < width:
            grid[row][col] = "☼"

        row, col = to_cell(x_values[-1], y_values[-1])
        if 0 <= row < height and 0 <= col < width:
            grid[row][col] = "O"

        return "\n".join("".join(row) for row in grid)

    # This gives the cleanest without flicker
    # Make it so that the speed will change the frame delay

    @staticmethod
    def animate(t, x, y, speed=1, frame_delay=0.05):
        if speed <= 0:
            raise ValueError("Speed must be greater than zero.")

        width, height = 250, 35
        points_per_frame = max(1, round(speed))

        # Clear once and hide the cursor.
        sys.stdout.write("\033[2J\033[?25l")
        sys.stdout.flush()

        try:
            for i in range(0, len(t), points_per_frame):
                frame = ConsoleRender.make_frame(
                    x[:i + 1], y[:i + 1], 0, 0,
                    width=width, height=height
                )

                # One write replaces the same fixed-size box each frame.
                sys.stdout.write("\033[H" + frame)
                sys.stdout.flush()
                time.sleep(frame_delay)
        finally:
            # Put the cursor below the grid and show it again.
            sys.stdout.write(f"\033[{height + 1};1H\033[?25h")
            sys.stdout.flush()

