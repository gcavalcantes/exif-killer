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
            if checkFileType(file_path):

                # Detects existing exif data
                if checkExif(image):
                    pass
                    # TODO Erases the exif data
                    # TODO Checks if the data has been erased
                    # TODO Show message that confirms that the data has bee erased.
                else:
                    # remove in production
                    print("Exif data could not be detected. Ending operations.")
    else:
        print("File could not be found. Ending operations.")
        pass


# Check if the file is of a valid format
def checkFileType(file):
    # List of accepted extensions
    accepted_extensions = [".png", ".jpg", ".jfif", ".jpeg", ".bmp"]
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
        print(f"Image {status}")
        return True
    else:
        status = "does not contain any EXIF information."
        print(f"Image {status}")
        return False
    

# Testing the function
exifKiller('/Users/Cliente/Pictures/Saved Pictures/bsg1.jpg ')
