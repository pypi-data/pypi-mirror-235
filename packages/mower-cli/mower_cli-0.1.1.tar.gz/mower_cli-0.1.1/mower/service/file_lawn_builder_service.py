from mower.service.lawn_builder_service import LawnBuilderService


class FileLawnBuilderService(LawnBuilderService):

    def __init__(self, file_path: str):
        with open(file_path) as file:
            lines = [line.rstrip('\n') for line in file.readlines()]
            super().__init__(lines)
