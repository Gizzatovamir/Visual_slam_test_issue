import plotly.graph_objs as go
import pandas as pd
import pathlib
import sys


def read_csv(file_path: pathlib.Path) -> pd.DataFrame:
    return pd.read_csv(file_path.as_posix())


def draw_point_cloud(df: pd.DataFrame) -> None:
    print(df['x'])
    print(df['y'])
    print(df['z'])
    fig = go.Figure(data=go.Scatter3d(x=df["x"].to_list(), y=df["y"].to_list(), z=df["z"].to_list(), mode='markers'))
    fig.show()
    fig.to_html("point_cloud.html")


if __name__ == "__main__":
    argv = sys.argv

    if len(argv) < 2:
        print("Needs more vars")

    else:
        bin_fn = argv[1]
        df = read_csv(pathlib.Path(bin_fn))
        draw_point_cloud(df)
