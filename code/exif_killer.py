import os.path
from exif import Image


def exifKiller(file_path):
    # Check if the file exists
    if os.path.isfile(file_path):
        # remove in production
        print("File exists. Proceding with operations...")
        # Copies the file
        with open(file_path, "rb") as file_image:
            # remove in production
            image = Image(file_image)
            print("File successfuly opened. Proceding... ")
            checkFileType(file_path)
            # Detects existing exif data
            checkExif(image)
    # TODO Erases the exif data
    # TODO Checks if the data has been erased
    # TODO Show message that confirms that the data has bee erased.
    else:
        print("File could not be found. Ending operations.")
        pass


# TODO Check if the file is of a valid format
def checkFileType(file):
    # List of accepted extensions
    accepted_extensions = [".png", ".jpg", ".jfif", ".jpeg", ".bmp", "", "", "", ""]
    # TODO Checks if the file is in a valid format
    file_name, file_extension = os.path.splitext(file)
    if file_extension in accepted_extensions :
        # remove in production
        print("File extension for {} is accepted. Proceding...".format(file_name + file_extension))
        return True
    else:
        return False
    #print("File Type is: {} ".format(file_extension)) # remove on production
    #print("File Name is: {} ".format(file_name)) # remove on production

# Detects existing exif data
def checkExif(image):
    status = ''
    if image.has_exif:
        status = f"contains EXIF (version {image.exif_version}) information."
    else:
        status = "does not contain any EXIF information."
    print(f"Image {status}")

# Testing the function
exifKiller('/Users/Cliente/Pictures/Saved Pictures/bsg1.jpg ')
