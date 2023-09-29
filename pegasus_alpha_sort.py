# Define the path to your Pegasus metadata file
metadata_file = r"C:/Roms/Super Nintendo Entertainment System/metadata.txt"

# Empty string and dict to eventually hold our initial read of the metadata
beginning_data = ''
metadata_entries = {}

# This is seriously so gross and messy I can't even be bothered commenting it properly XD
# It works though
with open(metadata_file, "r") as file:
    get_beginning_data = 1
    game_being_parsed = None
    add_game_data_to_dict = 0
    for line in file:
        if line.startswith("game: "):
            get_beginning_data = 0
            game_entry = line.split("game: ")[1].split("\n")[0]
            if " : " in game_entry:
                game_entry = game_entry.replace(" : ", ": ")
            game_being_parsed = game_entry
            metadata_entries[game_being_parsed] = ""
            add_game_data_to_dict = 1
            continue
        if line == "\n" and add_game_data_to_dict == 1:
            add_game_data_to_dict = 0
            game_being_parsed = None
        if add_game_data_to_dict == 1:
            metadata_entries[game_being_parsed] += line
        if get_beginning_data == 1:
            beginning_data += line

# Strip the ending newlines off the end of each entry
# since we're going to add our own standardized amount of new-lines on rewriting
for each_entry in metadata_entries:
    if metadata_entries[each_entry].endswith("\n"):
        metadata_entries[each_entry] = metadata_entries[each_entry][:-1]

# See above
while beginning_data.endswith("\n"):
    beginning_data = beginning_data[:-1]

# Append the console/system metadata and launch parameters
with open(metadata_file, "w") as f:
    f.write(beginning_data)
    f.write("\n\n")

# Sort dict entries alphabetically
metadata_entries_sorted = sorted(metadata_entries.items())

# Create an iterator counter to avoid appending new-lines at end of the file
total_num_of_entries = len(metadata_entries_sorted)
iterate_count = 0
print(total_num_of_entries)

# Append the sorted metadata entries back into the file
for key, value in metadata_entries_sorted:
    iterate_count +=1
    with open(metadata_file, "a") as f:
        f.write("game: " + key + "\n")
        f.write(value)
        if iterate_count != total_num_of_entries:
            f.write("\n\n")