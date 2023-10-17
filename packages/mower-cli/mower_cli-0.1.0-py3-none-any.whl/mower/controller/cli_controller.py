from argparse import ArgumentParser

from mower.service.file_lawn_builder_service import FileLawnBuilderService
from mower.service.mowing_service import MowingService


def main():
    args = get_parser()
    lawn = FileLawnBuilderService(args.config).lawn
    MowingService(lawn).run_all_actions()
    print(lawn.get_mowers_short_locations())


def get_parser():
    args_parser = ArgumentParser()
    args_parser.add_argument("--config",
                             help="Specify the path to the mower config",
                             required=True
                             )
    return args_parser.parse_args()


if __name__ == '__main__':
    main()
