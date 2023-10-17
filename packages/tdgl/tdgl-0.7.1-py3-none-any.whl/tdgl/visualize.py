import argparse
import logging
import os

from .visualization import (
    DEFAULT_QUANTITIES,
    InteractivePlot,
    MultiInteractivePlot,
    Quantity,
    create_animation,
    monitor_solution,
)

logger = logging.getLogger("visualize")


def make_parser():
    parser = argparse.ArgumentParser(description="Visualize TDGL simulation data.")
    subparsers = parser.add_subparsers()
    parser.add_argument("--input", type=str, help="H5 file to visualize.")
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Run in verbose mode.",
    )
    parser.add_argument(
        "-s",
        "--silent",
        action="store_true",
        help="Run in silent mode.",
    )
    parser.add_argument(
        "--dimensionless", action="store_true", help="Use dimensionless x-y units."
    )
    parser.add_argument(
        "--axis-labels", action="store_true", help="Add x-y axis labels."
    )

    interactive_parser = subparsers.add_parser(
        "interactive", help="Create an interactive plot of one or more quantities."
    )
    interactive_parser.add_argument(
        "-q",
        "--quantities",
        type=lambda s: str(s).upper(),
        choices=Quantity.get_keys() + ["ALL"],
        nargs="*",
        help=(
            "Name(s) of the quantities to show. Because 'quantities' takes a "
            "variable number of arguments, it must be the last argument provided."
        ),
    )

    interactive_parser.set_defaults(func=visualize_tdgl)

    animate_parser = subparsers.add_parser(
        "animate", help="Create an animation of the TDGL data."
    )
    animate_parser.add_argument(
        "-o", "--output", type=str, help="Output file for animation."
    )
    animate_parser.add_argument(
        "-f", "--fps", type=int, default=30, help="Frame rate of the animation."
    )
    animate_parser.add_argument(
        "-d", "--dpi", type=float, default=200, help="Resolution in dots per inch."
    )
    animate_parser.add_argument(
        "--figsize",
        type=float,
        nargs=2,
        default=None,
        help="Figure size (width, height) in inches.",
    )
    animate_parser.add_argument(
        "--min-frame",
        type=int,
        default=0,
        help="The first frame to render.",
    )
    animate_parser.add_argument(
        "--max-frame",
        type=int,
        default=-1,
        help="The last frame to render (-1 indicates the last step in the simulation).",
    )
    animate_parser.add_argument(
        "--autoscale",
        action="store_true",
        help="Autoscale colorbar limits at each frame.",
    )
    animate_parser.add_argument(
        "--axes-off",
        action="store_true",
        help="Turn the axes off.",
    )
    animate_parser.add_argument(
        "--title-off",
        action="store_true",
        help="Turn figure title off.",
    )
    animate_parser.add_argument(
        "-q",
        "--quantities",
        type=lambda s: str(s).upper(),
        choices=Quantity.get_keys() + ["ALL"],
        nargs="*",
        help=(
            "Name(s) of the quantities to show. Because ``quantities`` takes a "
            "variable number of arguments, it must be the last argument provided."
        ),
    )
    animate_parser.set_defaults(func=animate_tdgl)

    monitor_parser = subparsers.add_parser(
        "monitor", help="Visualize the results of a simulation as it is running."
    )
    monitor_parser.add_argument(
        "--autoscale",
        action="store_true",
        help="Autoscale colorbar limits at each frame.",
    )
    monitor_parser.add_argument(
        "--figsize",
        type=float,
        nargs=2,
        default=None,
        help="Figure size (width, height) in inches.",
    )
    monitor_parser.add_argument(
        "-q",
        "--quantities",
        type=lambda s: str(s).upper(),
        choices=Quantity.get_keys() + ["ALL"],
        nargs="*",
        help=(
            "Name(s) of the quantities to show. Because ``quantities`` takes a "
            "variable number of arguments, it must be the last argument provided."
        ),
    )
    monitor_parser.set_defaults(func=monitor_tdgl)

    return parser


def animate_tdgl(args):
    kwargs = dict(
        input_file=args.input,
        output_file=args.output,
        logger=logger,
        silent=args.silent,
        dpi=args.dpi,
        fps=args.fps,
        min_frame=args.min_frame,
        max_frame=args.max_frame,
        autoscale=args.autoscale,
        dimensionless=args.dimensionless,
        axis_labels=args.axis_labels,
        axes_off=args.axes_off,
        title_off=args.title_off,
    )
    if args.figsize is not None:
        kwargs["figure_kwargs"] = dict(figsize=args.figsize)
    if args.quantities is None or "ALL" in args.quantities:
        kwargs["quantities"] = DEFAULT_QUANTITIES
    else:
        kwargs["quantities"] = args.quantities
    create_animation(**kwargs)


def visualize_tdgl(args):
    if args.quantities is None:
        InteractivePlot(
            input_file=args.input,
            dimensionless=args.dimensionless,
            axis_labels=args.axis_labels,
            logger=logger,
        ).show()
        return
    kwargs = dict(
        input_file=args.input,
        dimensionless=args.dimensionless,
        axis_labels=args.axis_labels,
        logger=logger,
    )
    if "ALL" not in args.quantities:
        kwargs["quantities"] = args.quantities
    MultiInteractivePlot(**kwargs).show()


def monitor_tdgl(args):
    dirname = os.path.dirname(args.input)
    fname = os.path.basename(args.input) + ".tmp"
    h5path = os.path.join(dirname, fname)
    kwargs = dict(
        h5path=h5path,
        autoscale=args.autoscale,
        dimensionless=args.dimensionless,
    )
    if args.figsize is not None:
        kwargs["figure_kwargs"] = dict(figsize=args.figsize)
    if args.quantities is None or "ALL" in args.quantities:
        kwargs["quantities"] = DEFAULT_QUANTITIES
    else:
        kwargs["quantities"] = args.quantities
    monitor_solution(**kwargs)


def main(args):
    logger.setLevel(logging.DEBUG if args.verbose else logging.INFO)
    logger.disabled = args.silent
    args.func(args)


if __name__ == "__main__":
    main(make_parser().parse_args())
