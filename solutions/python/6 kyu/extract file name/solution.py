class FileNameExtractor:
    @staticmethod
    def extract_file_name(dirty_file_name):
        return '.'.join(dirty_file_name.split('.')[:-1]).split('_', maxsplit=1)[1]