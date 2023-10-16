import chardet


def checkEncoding(filepath: str):
    """Checks the encoding of a file using chardet\n
    @param:`filepath`: Path of the file of which encoding needs to be checked.\n
    @return: Returns the encoding of the file or if no proper encoding is detected then returns false.\n
    """
    with open(filepath, "rb") as raw_file:
        detector = chardet.universaldetector.UniversalDetector()
        for line in raw_file:
            detector.feed(line)
            if detector.done:
                break
        detector.close()
        return detector.result["encoding"]
