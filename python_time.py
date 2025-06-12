import time

def generate_file(filename, size_mb):
    line = "this is a line of text for benchmarking purposes.\n"
    count = (size_mb * 1024 * 1024) // len(line)

    start_time = time.time()
    with open(filename, "w") as f:
        for _ in range(count):
            f.write(line)
    end_time = time.time()

    return round(end_time - start_time, 2)

def convert_to_uppercase(input_file, output_file):
    start_time = time.time()
    with open(input_file, "r") as infile, open(output_file, "w") as outfile:
        for line in infile:
            outfile.write(line.upper())
    end_time = time.time()

    return round(end_time - start_time, 2)

sizes = [200, 400, 600, 800, 1000]
gen_times = []
conv_times = []

for size in sizes:
    input_name = f"input_{size}MB.txt"
    output_name = f"output_{size}MB.txt"

    print(f"\nGenerating {input_name}...")
    gen_time = generate_file(input_name, size)
    print(f"Generated {size}MB in {gen_time} sec")

    print(f"Converting {input_name} to uppercase...")
    conv_time = convert_to_uppercase(input_name, output_name)
    print(f"Converted {size}MB in {conv_time} sec")

    gen_times.append(gen_time)
    conv_times.append(conv_time)

print("\nGeneration times (sec):", gen_times)
print("Conversion times (sec):", conv_times)
