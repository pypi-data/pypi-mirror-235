"""Completes the tasks specified in the arg_parser."""
import argparse
from simplt.dotted_plot.dotted_plot import example_create_multi_group_dotted_plot

from typeguard import typechecked

from simplt.box_plot.box_plot import example_box_plot
from simplt.export_plot import create_target_dir_if_not_exists
from simplt.latex_table.latex_table import example_create_a_table
from simplt.line_plot.line_plot import example_create_multi_line_plot


@typechecked
def process_args(args: argparse.Namespace, default_output_path: str) -> None:
    """Processes the arguments and ensures the accompanying tasks are
    executed."""
    # Create output path.
    create_target_dir_if_not_exists(default_output_path)
    print(f"TODO: create: {default_output_path}")

    # Delete output images if desired.
    if args.remove_images:
        print("TODO: delete images.")

    if args.box_plot:
        example_box_plot(
            extensions=[
                ".png",
            ],
            filename="example_box",
            output_dir=default_output_path,
        )

    if args.line_plot:
        example_create_multi_line_plot(
            extensions=[
                ".png",
            ],
            filename="example_line",
            output_dir=default_output_path,
        )
    
    if args.dot_plot:
        example_create_multi_group_dotted_plot(
            extensions=[
                ".png",
            ],
            filename="example_dots",
            output_dir=default_output_path,
        )

    if args.latex_table:
        print("TODO: Create LaTex table.")
        example_create_a_table(
            filename="example", output_dir=default_output_path
        )
