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
            if checkFileType(file_path):
                image = Image(file_image)
                print("File successfuly opened. Proceding... ")

                # Detects existing exif data
                if checkExif(image):
                    # remove in production
                    print("Exif data detected. Proceding...")
                    getExif(image)
                    # Erases the exif data
                    killExif(image)
                    # TODO Checks if the data has been erased
                    # TODO Show message that confirms that the data has bee erased.
                else:
                    # remove in production
                    print("Exif data could not be detected. Ending operations.")
            else:
                print("File type invalid. Ending operations.")
    else:
        print("File could not be found. Ending operations.")
        pass

# Check if the file is of a valid format
def checkFileType(file):
    # List of accepted extensions
    accepted_extensions = [".png", '.jpg', ".jfif", ".jpeg", ".bmp"]
    file_name, file_extension = os.path.splitext(file)
    
    if file_extension.lower() in accepted_extensions :
        # remove in production
        print("File extension for {} is accepted. Proceding...".format(file_name + file_extension))
        return True
    else:
        return False
    #print("File Type is: {} ".format(file_extension)) # remove in production
    #print("File Name is: {} ".format(file_name)) # remove in production

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
    
# TODO Shows the exif data
def getExif(image):
    image_members = []
    image_members.append(dir(image))

    for index, image_member_list in enumerate(image_members):
        print(f"Image {index} contains {len(image_member_list)} members:")
        print(f"{image_member_list}\n")

# TODO Delete all relevant EXIF data
def killExif(image):
    #image.delete('gps_latitude')
    # remove in production
    print("EXIF data deleted")

# Testing the function
exifKiller('/Users/Cliente/Pictures/Saved Pictures/temp/bsg1.jpg')
