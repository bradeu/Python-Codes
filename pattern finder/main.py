import re
import os
import time

# CURRENT TIME BEFORE
start_time = time.time()

pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')

for folder, sub_file, files in os.walk('./extracted_content'):
    for file in files:
        current_file = open(folder+'/'+file, 'r')
        for match in re.finditer(pattern, current_file.read()):
            print(match.group())
            print(file)
            print(folder)

# CURRENT TIME AFTER
end_time = time.time()

# ELAPSED TIME
elapsed_time = end_time - start_time
print(elapsed_time)

