import os
import subprocess
import sys

def generate_uml_with_pyreverse(file_path, output_format="puml", project_name="GeneratedDiagram"):
    """
    Generate UML diagrams using pyreverse and save them in the specified format.
    """
    if not os.path.exists(file_path):
        print(f"Error: File or directory {file_path} does not exist.")
        sys.exit(1)

    try:
        # Run the pyreverse command
        subprocess.run(
            ["pyreverse", "-o", output_format, "-p", project_name, file_path],
            check=True
        )
        print(f"UML diagram saved as {project_name}.{output_format}")
      #  if output_format == "puml":
          
        # else:
        #     print(f"UML diagrams generated: classes.{output_format}, packages.{output_format}")
    except subprocess.CalledProcessError as e:
        print(f"Error: pyreverse command failed. {e}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <python_file_or_directory>")
        sys.exit(1)

    file_path = sys.argv[1]
    generate_uml_with_pyreverse(file_path)

if __name__ == "__main__":
    main()
