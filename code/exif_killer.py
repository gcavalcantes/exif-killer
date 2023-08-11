import os.path
from exif import Image

def exifKiller(file_path):
    # Check if the file exists
    if os.path.isfile(file_path):
        # Copies the file
        with open(file_path, "rb") as file_image:
            if checkFileType(file_path):
                image = Image(file_image)
                # Detects existing exif data
                if checkExif(image):
                    getExif(image)
                    # Erases the exif data
                    killExif(image)
                    saveChanges(image, file_path)

                else:
                    # TODO If no exif data is detected, show message and end operations.
                    pass
            else:
                # TODO If file type is incorrect, show error message and end operations.
                pass
    else:
        # TODO If path to file cannot be found, show error message and end operations.
        pass

# Check if the file is of a valid format


def checkFileType(file):
    # List of accepted extensions
    accepted_extensions = [".png", '.jpg', ".jfif", ".jpeg", ".bmp"]
    file_name, file_extension = os.path.splitext(file)

    if file_extension.lower() in accepted_extensions:
        return True
    else:
        return False

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

# Shows the exif data


def getExif(image):
    image_members = []
    image_members.append(dir(image))

    print("\nMaker: {}".format(image.make))
    print("\nSoftware: {}".format(image.software))
    print("\nF Number: {}".format(image.f_number))
    print("\nDate: {}".format(image.datetime))
    print("\nDate of digitization: {}".format(image.datetime_digitized))
    print("\nModel: " + image.model + "\n")

    for index, image_member_list in enumerate(image_members):
        print(f"Image {index} contains {len(image_member_list)} members:")
        print(f"{image_member_list}\n")

# Delete all relevant EXIF data


def killExif(image):
    try:
        image.delete_all()

    except TypeError as errorType:
        print(errorType)
    except AttributeError as errorAttribute:
        print(errorAttribute)

# List the available information keys of an image


def listInfo(image):
    image_members = []
    image_members.append(dir(image))

    for index, image_member_list in enumerate(image_members):
        print(f"Image {index} contains {len(image_member_list)} members:")
        print(f"{image_member_list}\n")

# Save the changes made to the image


def saveChanges(image, image_path):
    with open(image_path, 'wb') as updated_image_file:
        updated_image_file.write(image.get_file())

