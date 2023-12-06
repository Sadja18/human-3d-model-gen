import os
import shutil

# Source directory path
source_dir = './data/my-dataset/generated'

# Destination directory path
destination_dir = './data/nomo/prepared/female'

# Counter for female directories processed
female_directories_processed = 0

# Iterate through 'female' directories in the source directory
for root, dirs, files in os.walk(source_dir):
    for directory_name in dirs:
        # Check if the directory matches the pattern for females
        if directory_name.startswith('female'):
            female_subdir_path = os.path.join(root, directory_name)
            # Check if 'gender.npy' exists inside the 'female' subdirectory
            if os.path.exists(os.path.join(female_subdir_path, 'gender.npy')) and os.path.exists(os.path.join(female_subdir_path, 'shape.npy')):
                # Source paths for files
                gender_file_path = os.path.join(female_subdir_path, 'gender.npy')
                shape_file_path = os.path.join(female_subdir_path, 'shape.npy')

                # Destination paths for files
                destination_gender_file = os.path.join(destination_dir, f'{directory_name}_gender.npy')
                destination_shape_file = os.path.join(destination_dir, f'{directory_name}_shape.npy')

                # Print the file movement details
                print(f"Moving '{gender_file_path}' from '{female_subdir_path}' to '{destination_gender_file}'")
                print(f"Moving '{shape_file_path}' from '{female_subdir_path}' to '{destination_shape_file}'")

                try:
                    # Move files to the destination directory with renamed filenames
                    shutil.move(gender_file_path, destination_gender_file)
                    shutil.move(shape_file_path, destination_shape_file)
                    print("Files moved successfully!")
                except Exception as e:
                    print(f"An error occurred: {e}")

                # Increment the female directories counter
                female_directories_processed += 1

                # Check if 100 female directories have been processed
                if female_directories_processed == 100:
                    break
            else:
                print('hj ', os.path.exists(os.path.join(female_subdir_path, 'gender.npy')),  "and ", os.path.exists(os.path.join(female_subdir_path, 'shape.npy')))
    if female_directories_processed == 100:
        break
