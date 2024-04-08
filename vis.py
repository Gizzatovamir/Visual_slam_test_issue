import plotly.graph_objs as go
import pandas as pd
import pathlib
import sys


def read_csv(file_path: pathlib.Path) -> pd.DataFrame:
    return pd.read_csv(file_path.as_posix())


def draw_trajectory(input_path: str, out_path: str) -> None:
    def write_2d_trajectory(first_list: list, second_list: list, file_name: str):
        with open(file_name, "w") as f:
            for x, y in zip(first_list, second_list):
                f.write(f"{x}, {y}\n")

    with open(input_path, "r") as trajectory:
        lines = trajectory.readlines()
        x, y, z = list(), list(), list()
        for row in lines:
            line = row.replace("\n", "").split(" ")
            x.append(line[1])
            y.append(line[2])
            z.append(line[3])
        fig = go.Figure(
            data=go.Scatter3d(
                x=x,
                y=y,
                z=z,
                mode="markers",
            )
        )
        write_2d_trajectory(x, y, "x_y_trajectory.txt")
        write_2d_trajectory(x, z, "x_z_trajectory.txt")
        write_2d_trajectory(y, z, "y_z_trajectory.txt")
        fig.write_html(out_path)
        fig.show()


def draw_point_cloud(df: pd.DataFrame, out_path: str) -> None:
    fig = go.Figure(
        data=go.Scatter3d(
            x=df["x"].to_list(),
            y=df["y"].to_list(),
            z=df["z"].to_list(),
            mode="markers",
        )
    )
    fig.write_html(out_path)
    fig.show()


if __name__ == "__main__":
    argv = sys.argv

    if len(argv) < 2:
        print("Needs more vars")

    else:
        bin_fn = argv[1]
        # df = read_csv(pathlib.Path(bin_fn))
        # draw_point_cloud(df, argv[2])
        draw_trajectory(argv[1], argv[2])
