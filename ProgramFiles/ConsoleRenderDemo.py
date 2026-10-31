import math
import shutil
import sys
import time


class ConsoleRender:

    @staticmethod
    def make_frame(
        x_values, y_values, sun_x, sun_y,
        width, height, extent, marker="P"
    ):
        # Leave one terminal column unused to avoid automatic line wrapping.
        width = max(10, width - 1)
        height = max(5, height)

        scale = min(
            (width - 1) / (2 * extent),
            (height - 1) / (2 * extent)
        )

        grid = [[" " for _ in range(width)] for _ in range(height)]

        def to_cell(x, y):
            col = round((width - 1) / 2 + x * scale)
            row = round((height - 1) / 2 - y * scale)
            return row, col

        # Draw the trail.
        for x_pos, y_pos in zip(x_values, y_values):
            row, col = to_cell(x_pos, y_pos)
            if 0 <= row < height and 0 <= col < width:
                grid[row][col] = "."

        # Draw the Sun and current planet over the trail.
        row, col = to_cell(sun_x, sun_y)
        if 0 <= row < height and 0 <= col < width:
            grid[row][col] = "S"

        row, col = to_cell(x_values[-1], y_values[-1])
        if 0 <= row < height and 0 <= col < width:
            grid[row][col] = marker

        return "\n".join("".join(row) for row in grid)

    @staticmethod
    def animate(t, x, y, fullscreen=True, frame_delay=0.05, marker="P"):
        if len(t) == 0:
            raise ValueError("There are no simulation points to animate.")
        if frame_delay <= 0:
            raise ValueError("Frame delay must be greater than zero.")

        # Read the terminal size at runtime.
        terminal = shutil.get_terminal_size(fallback=(80, 24))

        if fullscreen:
            width = terminal.columns - 1
            height = terminal.lines - 2
        else:
            width = min(80, terminal.columns - 1)
            height = min(24, terminal.lines - 2)

        # Use one scale for the entire orbit, not just the trail seen so far.
        extent = max(
            max(abs(value) for value in x),
            max(abs(value) for value in y),
            1.0
        ) * 1.1

        points_per_frame = 1

        sys.stdout.write("\033[2J\033[?25l")
        sys.stdout.flush()

        try:
            for i in range(0, len(t), points_per_frame):
                frame = ConsoleRender.make_frame(
                    x[:i + 1], y[:i + 1], 0, 0,
                    width=width,
                    height=height,
                    extent=extent,
                    marker=marker
                )
                sys.stdout.write("\033[H" + frame)
                sys.stdout.flush()
                time.sleep(frame_delay)
        finally:
            sys.stdout.write(f"\033[{height + 1};1H\033[?25h")
            sys.stdout.flush()